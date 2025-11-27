import os
import sys
from enum import Enum
from pathlib import Path

labels: dict[str, bytes] = {}
checkLabels: dict[int, str] = {}
bytesWritten: int = 0
outBytes: bytes = b''

registers: dict[str, int] = {
	"reg0" : 0,
	"r0" : 0,
	"reg1" : 1,
	"r1" : 1,
	"reg2" : 2,
	"r2" : 2,
	"reg3" : 3,
	"r3" : 3,
	"reg4" : 4,
	"r4" : 4,
	"reg5" : 5,
	"r5" : 5,
	"reg6" : 6,
	"r6" : 6
}

def IsValidHex(string: str) -> bool:
	string = string.lower()

	if not string.startswith("0x"):
		return False
	for char in string[2:]:
		if not "0123456789abcdef".__contains__(char):
			return False
	return True
def IsValidBin(string: str) -> bool:
	string = string.lower()

	if not string.startswith("0b"):
		return False
	for char in string[2:]:
		if not "01".__contains__(char):
			return False
	return True

def IsValidImmediate(string: str) -> bool:
	return string.isdigit() or IsValidBin(string) or IsValidHex(string)
def GetImmediateBase(string: str) -> int:
	if IsValidHex(string): return 16
	if IsValidBin(string): return 2
	if IsValidImmediate(string): return 10
	return -1

class ArgType(Enum):
	IMMEDIATE = 0
	REGISTER = 1
	MEMORY_ADDR = 2
	NONE = 3

def argumentStringToType(arg: str, argIndex: int) -> ArgType:
	global bytesWritten
	if arg.startswith("["):
		if not arg.endswith("]"):
			raise Exception("Error: Bracket not closed:", arg)
		if not IsValidImmediate(arg[1:-1]):
			raise Exception("Error: Expected immediate or label but got", arg)
		return ArgType.MEMORY_ADDR
	if labels.__contains__(arg):
		return ArgType.IMMEDIATE
	
	if registers.__contains__(arg):
		return ArgType.REGISTER
	if IsValidImmediate(arg):
		return ArgType.IMMEDIATE
	if arg == "":
		return ArgType.NONE
	
	checkLabels[bytesWritten+argIndex+1] = arg
	return ArgType.IMMEDIATE


Aliases: dict[str, str] = {
	"je": "jz",
	"jne": "jnz",
	"jnle": "jg",
	"jnl": "jge",
	"jnge": "jl",
	"jng": "jle",
	"jnbe": "ja",
	"jnb": "jae",
	"jnc": "jae",
	"jnae": "jb",
	"jc": "jb",
	"jna": "jbe",
	"jpe": "jp",
	"jpo": "jnp",
}
Args: dict[str, list[list[ArgType]]] = {
	"nop": [],
	"mov": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"add": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"sub": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"mul": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"div": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"push": [[ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"pop": [[ArgType.REGISTER,ArgType.MEMORY_ADDR]],   
	"shl": [[ArgType.REGISTER], [ArgType.IMMEDIATE,ArgType.REGISTER]],
	"shr": [[ArgType.REGISTER], [ArgType.IMMEDIATE,ArgType.REGISTER]],
	"and": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"or": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"xor": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"not": [[ArgType.REGISTER,ArgType.MEMORY_ADDR]],   
	"cmp": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.IMMEDIATE,ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"xchg": [[ArgType.REGISTER,ArgType.MEMORY_ADDR], [ArgType.REGISTER,ArgType.MEMORY_ADDR]],
	"jmp": [[ArgType.IMMEDIATE,ArgType.REGISTER]],     
	"jz": [[ArgType.IMMEDIATE,ArgType.REGISTER]],      
	"jnz": [[ArgType.IMMEDIATE,ArgType.REGISTER]],     
	"js": [[ArgType.IMMEDIATE,ArgType.REGISTER]],      
	"jns": [[ArgType.IMMEDIATE,ArgType.REGISTER]],     
	"jg": [[ArgType.IMMEDIATE,ArgType.REGISTER]],      
	"jge": [[ArgType.IMMEDIATE,ArgType.REGISTER]],     
	"jl": [[ArgType.IMMEDIATE,ArgType.REGISTER]],      
	"jle": [[ArgType.IMMEDIATE,ArgType.REGISTER]],     
	"ja": [[ArgType.IMMEDIATE,ArgType.REGISTER]],      
	"jae": [[ArgType.IMMEDIATE,ArgType.REGISTER]],     
	"jb": [[ArgType.IMMEDIATE,ArgType.REGISTER]],      
	"jbe": [[ArgType.IMMEDIATE,ArgType.REGISTER]],     
	"jp": [[ArgType.IMMEDIATE,ArgType.REGISTER]],      
	"jnp": [[ArgType.IMMEDIATE,ArgType.REGISTER]],     
	"jo": [[ArgType.IMMEDIATE,ArgType.REGISTER]],
	"jno": [[ArgType.IMMEDIATE,ArgType.REGISTER]]
}
Syntax: dict[str, str] = {
	"nop": "",
	"mov": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"add": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"sub": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"mul": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"div": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"push": "<IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"pop": "<REGISTER,MEMORY_ADDR>",
	"shl": "<REGISTER>, <IMMEDIATE,REGISTER>",
	"shr": "<REGISTER>, <IMMEDIATE,REGISTER>",
	"and": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"or": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"xor": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"not": "<REGISTER,MEMORY_ADDR>",
	"cmp": "<REGISTER,MEMORY_ADDR>, <IMMEDIATE,REGISTER,MEMORY_ADDR>",
	"xchg": "REGISTER,ArgType.MEMORY_ADDR], [ArgType.REGISTER,MEMORY_ADDR",
	"jmp": "<IMMEDIATE,REGISTER>",
	"jz": "<IMMEDIATE,REGISTER>",
	"jnz": "<IMMEDIATE,REGISTER>",
	"js": "<IMMEDIATE,REGISTER>",
	"jns": "<IMMEDIATE,REGISTER>",
	"jg": "<IMMEDIATE,REGISTER>",
	"jge": "<IMMEDIATE,REGISTER>",
	"jl": "<IMMEDIATE,REGISTER>",
	"jle": "<IMMEDIATE,REGISTER>",
	"ja": "<IMMEDIATE,REGISTER>",
	"jae": "<IMMEDIATE,REGISTER>",
	"jb": "<IMMEDIATE,REGISTER>",
	"jbe": "<IMMEDIATE,REGISTER>",
	"jp": "<IMMEDIATE,REGISTER>",
	"jnp": "<IMMEDIATE,REGISTER>",
	"jo": "<IMMEDIATE,REGISTER>",
	"jno": "<IMMEDIATE,REGISTER>"
}
InstrucID: dict[tuple[str, ArgType, ArgType], int] = {
	("nop", ArgType.NONE, ArgType.NONE): 0,
	("mov", ArgType.REGISTER, ArgType.IMMEDIATE): 1,
	("mov", ArgType.REGISTER, ArgType.REGISTER): 2,
	("mov", ArgType.REGISTER, ArgType.MEMORY_ADDR): 3,
	("mov", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 4,
	("mov", ArgType.MEMORY_ADDR, ArgType.REGISTER): 5,
	("mov", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 6,
	("add", ArgType.REGISTER, ArgType.IMMEDIATE): 7,
	("add", ArgType.REGISTER, ArgType.REGISTER): 8,
	("add", ArgType.REGISTER, ArgType.MEMORY_ADDR): 9,
	("add", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 10,
	("add", ArgType.MEMORY_ADDR, ArgType.REGISTER): 11,
	("add", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 12,
	("sub", ArgType.REGISTER, ArgType.IMMEDIATE): 13,
	("sub", ArgType.REGISTER, ArgType.REGISTER): 14,
	("sub", ArgType.REGISTER, ArgType.MEMORY_ADDR): 15,
	("sub", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 16,
	("sub", ArgType.MEMORY_ADDR, ArgType.REGISTER): 17,
	("sub", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 18,
	("mul", ArgType.REGISTER, ArgType.IMMEDIATE): 19,
	("mul", ArgType.REGISTER, ArgType.REGISTER): 20,
	("mul", ArgType.REGISTER, ArgType.MEMORY_ADDR): 21,
	("mul", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 22,
	("mul", ArgType.MEMORY_ADDR, ArgType.REGISTER): 23,
	("mul", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 24,
	("div", ArgType.REGISTER, ArgType.IMMEDIATE): 25,
	("div", ArgType.REGISTER, ArgType.REGISTER): 26,
	("div", ArgType.REGISTER, ArgType.MEMORY_ADDR): 27,
	("div", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 28,
	("div", ArgType.MEMORY_ADDR, ArgType.REGISTER): 29,
	("div", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 30,
	("push", ArgType.IMMEDIATE, ArgType.NONE): 31,
	("push", ArgType.REGISTER, ArgType.NONE): 32,
	("push", ArgType.MEMORY_ADDR, ArgType.NONE): 33,
	("pop", ArgType.REGISTER, ArgType.NONE): 34,
	("pop", ArgType.MEMORY_ADDR, ArgType.NONE): 35,
	("shl", ArgType.REGISTER, ArgType.IMMEDIATE): 36,
	("shl", ArgType.REGISTER, ArgType.REGISTER): 37,
	("shr", ArgType.REGISTER, ArgType.IMMEDIATE): 38,
	("shr", ArgType.REGISTER, ArgType.REGISTER): 39,
	("and", ArgType.REGISTER, ArgType.IMMEDIATE): 40,
	("and", ArgType.REGISTER, ArgType.REGISTER): 41,
	("and", ArgType.REGISTER, ArgType.MEMORY_ADDR): 42,
	("and", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 43,
	("and", ArgType.MEMORY_ADDR, ArgType.REGISTER): 44,
	("and", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 45,
	("or", ArgType.REGISTER, ArgType.IMMEDIATE): 46,
	("or", ArgType.REGISTER, ArgType.REGISTER): 47,
	("or", ArgType.REGISTER, ArgType.MEMORY_ADDR): 48,
	("or", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 49,
	("or", ArgType.MEMORY_ADDR, ArgType.REGISTER): 50,
	("or", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 51,
	("xor", ArgType.REGISTER, ArgType.IMMEDIATE): 52,
	("xor", ArgType.REGISTER, ArgType.REGISTER): 53,
	("xor", ArgType.REGISTER, ArgType.MEMORY_ADDR): 54,
	("xor", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 55,
	("xor", ArgType.MEMORY_ADDR, ArgType.REGISTER): 56,
	("xor", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 57,
	("not", ArgType.REGISTER, ArgType.NONE): 58,
	("not", ArgType.MEMORY_ADDR, ArgType.NONE): 59,
	("cmp", ArgType.REGISTER, ArgType.IMMEDIATE): 60,
	("cmp", ArgType.REGISTER, ArgType.REGISTER): 61,
	("cmp", ArgType.REGISTER, ArgType.MEMORY_ADDR): 62,
	("cmp", ArgType.MEMORY_ADDR, ArgType.IMMEDIATE): 63,
	("cmp", ArgType.MEMORY_ADDR, ArgType.REGISTER): 64,
	("cmp", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 65,
	("xchg", ArgType.REGISTER, ArgType.REGISTER): 66,
	("xchg", ArgType.REGISTER, ArgType.MEMORY_ADDR): 67,
	("xchg", ArgType.MEMORY_ADDR, ArgType.MEMORY_ADDR): 68,
	("jmp", ArgType.IMMEDIATE, ArgType.NONE): 69,
	("jmp", ArgType.REGISTER, ArgType.NONE): 70,
	("jz", ArgType.IMMEDIATE, ArgType.NONE): 71,
	("jz", ArgType.REGISTER, ArgType.NONE): 72,
	("jnz", ArgType.IMMEDIATE, ArgType.NONE): 73,
	("jnz", ArgType.REGISTER, ArgType.NONE): 74,
	("js", ArgType.IMMEDIATE, ArgType.NONE): 75,
	("js", ArgType.REGISTER, ArgType.NONE): 76,
	("jns", ArgType.IMMEDIATE, ArgType.NONE): 77,
	("jns", ArgType.REGISTER, ArgType.NONE): 78,
	("jg", ArgType.IMMEDIATE, ArgType.NONE): 79,
	("jg", ArgType.REGISTER, ArgType.NONE): 80,
	("jge", ArgType.IMMEDIATE, ArgType.NONE): 81,
	("jge", ArgType.REGISTER, ArgType.NONE): 82,
	("jl", ArgType.IMMEDIATE, ArgType.NONE): 83,
	("jl", ArgType.REGISTER, ArgType.NONE): 84,
	("jle", ArgType.IMMEDIATE, ArgType.NONE): 85,
	("jle", ArgType.REGISTER, ArgType.NONE): 86,
	("ja", ArgType.IMMEDIATE, ArgType.NONE): 87,
	("ja", ArgType.REGISTER, ArgType.NONE): 88,
	("jae", ArgType.IMMEDIATE, ArgType.NONE): 89,
	("jae", ArgType.REGISTER, ArgType.NONE): 90,
	("jb", ArgType.IMMEDIATE, ArgType.NONE): 91,
	("jb", ArgType.REGISTER, ArgType.NONE): 92,
	("jbe", ArgType.IMMEDIATE, ArgType.NONE): 93,
	("jbe", ArgType.REGISTER, ArgType.NONE): 94,
	("jp", ArgType.IMMEDIATE, ArgType.NONE): 95,
	("jp", ArgType.REGISTER, ArgType.NONE): 96,
	("jnp", ArgType.IMMEDIATE, ArgType.NONE): 97,
	("jnp", ArgType.REGISTER, ArgType.NONE): 98,
	("jo", ArgType.IMMEDIATE, ArgType.NONE): 99,
	("jo", ArgType.REGISTER, ArgType.NONE): 100,
	("jno", ArgType.IMMEDIATE, ArgType.NONE): 101,
	("jno", ArgType.REGISTER, ArgType.NONE): 102
}

class Argument:
	def __init__(self, arg:str, argIndex: int, type:ArgType = ArgType.NONE):
		self.arg = arg
		self.type = argumentStringToType(arg, argIndex) if (type == ArgType.NONE) else type
	@property
	def byte(self) -> bytes:
		match self.type:
			case ArgType.IMMEDIATE:
				if labels.__contains__(self.arg):
					return labels[self.arg]
				if self.arg in checkLabels.values():
					return b'\x00'
				return int(self.arg).to_bytes()
			case ArgType.REGISTER:
				return registers[self.arg].to_bytes()
			case ArgType.MEMORY_ADDR:
				return int(self.arg[1:-1], GetImmediateBase(self.arg[1:-1])).to_bytes()
			case ArgType.NONE:
				return b""
			case _:
				Exception(f"Internal Error: Unknown Argument: {self.arg}")
class Instruction:
	def __init__(self, instruction:str, args:list[Argument]):
		self.instruction = instruction
		self.args = args
	@property
	def isValid(self) -> bool:
		# check if valid instruction and correct amount and type of arguments
		argsValid: bool = True
		for i in range(len(self.args)):
			arg = self.args[i]
			if (not Args[arg.arg][i].__contains__(arg.type)):
				argsValid = False
				break
		return Args.__contains__(self.instruction) and argsValid and self.numArgs == len(Args[self.instruction])
	@property
	def instrucID(self) -> int:
		argBytes: bytes = b''
		
		return InstrucID[(self.instruction, self.args[0].type if len(self.args) > 0 else ArgType.NONE, self.args[1].type if len(self.args) > 1 else ArgType.NONE)]
	@property
	def numArgs(self) -> int:
		return len(self.args)
	@property
	def hex(self) -> bytes:
		argString: bytes = b''
		for arg in self.args:
			argString += arg.byte
		return self.instrucID.to_bytes() + argString
	@property
	def sytaxString(self) -> str:
		return f"{self.instruction} {Syntax[self.instruction]}"
	
	def __str__(self):
		argString: str = " , "*(len(self.args) > 0)
		for arg in self.args:
			argString += f"{arg.arg}, "
		return f"{self.instruction}{argString[2:-2]}"
	


def InvalidArgumentsException(instruc: Instruction) -> Exception:
	eString:str = f"Invalid Argument Exception: Expected {instruc.sytaxString} but got {str(instruc)}"

	return Exception(eString)

if len(sys.argv) < 2:
	raise Exception(
		'''No source file specified
		Syntax:
		lasm.py <source file path>
		''')
#print(sys.argv)

path: str = sys.argv[1]

if path.startswith('/'):
	path = os.getcwd() + path
#print(path)

# Read file in lines
with open(path) as file:
	script: list[str] = file.readlines()

# Split file into tokens, ignore comments
for i in range(len(script)):
	line = script[i]
	# Remove comments
	if line.__contains__(";"):
		line = line[:line.index(";")]

	# split by whitespace
	split = line.split()
	if len(split) < 1:
		continue

	# TODO: Implement Labels
	instruction: Instruction
	args: list[str] = []
	# Check for labels
	if split[0].__contains__(":"):
		#  Allow labels to have an instruction on the same line after the colon
		labelSplit: list[str] = split[0].split(":")

		labels[labelSplit[0]] = (bytesWritten).to_bytes()
		toRemove: list[int] = []
		for index in checkLabels:
			if checkLabels[index] == labelSplit[0]:
				toRemove.append(index)
				outBytes = outBytes[:index] + (bytesWritten).to_bytes() + outBytes[index+1:]
		for i in toRemove:
			del checkLabels[i]

		if len(labelSplit) > 2:
			raise Exception(f"Syntax Error: Expected instruction or newline but got {line}")
		print(f"{labelSplit[0]}: ->", (bytesWritten).to_bytes())
		split[0] = labelSplit[1]

	if split[0] == "":
		continue
	if not Args.__contains__(split[0]):
		if not Aliases.__contains__(split[0]):
			raise Exception(f"Unknown Instruction: {split[0]}")
		split[0] = Aliases[split[0]]

	for i in range(len(split[1:])):
		string = split[i+1]
		if string == "":
			continue

		if string.__contains__(","):
			args.extend(string.split(","))
		else:
			args.append(string)
		#print(string)

	argList: list[Argument] = []
	for i in range(len(args)):
		if args[i] == "":
			continue
		argList.append(Argument(args[i], i))
	instruction = Instruction(split[0], argList)

	bytesWritten += len(instruction.hex)
	print(instruction, "->", instruction.hex)
	#print("bytesWritten:", bytesWritten)
	outBytes += instruction.hex
	#print(line)


if len(checkLabels) > 0:
	for label in checkLabels:
		print("Unknown Argument:", label)

print("outBytes:", outBytes)
print(f"outPath: {os.path.dirname(path)}/{str(Path(path).stem)}.bin")
with open(f"{os.path.dirname(path)}/{str(Path(path).stem)}.bin", "bw") as outFile:
	outFile.write(outBytes)