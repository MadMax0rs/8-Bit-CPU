fileName = input("Script Name: ")
toWrite: str = "v3.0 hex words addressed\n00:"
with open("D:/Logisim/8-Bit-CPU/scripts/asm/" + fileName + ".bin", "rb") as file:
	for byte in file.read():
		hexStr: str = hex(byte)[2:]
		toWrite += " " + "0"*(2-len(hexStr)) + hexStr

with open("D:/Logisim/8-Bit-CPU/scripts/asm/" + fileName, "w") as file:
	file.write(toWrite)