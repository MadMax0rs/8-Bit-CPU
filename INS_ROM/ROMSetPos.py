import json

JSON = {}

with open("D:/DigitalLogicSim/python/8-Bit-CPU/INS_ROM/INS_ROM-original.json", "r", encoding="utf-8") as file:
	JSON = json.loads(file.read())

for Pin in range(len(JSON["OutputPins"])):
	JSON["OutputPins"][Pin]["Position"]["x"] = 30.0

with open("D:/DigitalLogicSim/python/8-Bit-CPU/INS_ROM/INS_ROM.json", "w", encoding="utf-8") as file:
	file.write(json.dumps(JSON).encode().decode('unicode-escape'))