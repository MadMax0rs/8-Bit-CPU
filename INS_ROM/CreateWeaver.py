import json


numInstructions = 256
numMicroinstructionLines = 10

JSON = {
	"DLSVersion": "2.1.6",
	"Name": "INS-ROM_WEAVER",
	"NameLocation": 0,
	"ChipType": 0,
	"Size": {
		"x": 1.775,
		"y": numInstructions * numMicroinstructionLines
	},
	"Colour": {
		"r": 0.6888899,
		"g": 0.5899531,
		"b": 0.240899935,
		"a": 1
	},
	"InputPins": [],
	"OutputPins": [],
	"SubChips": [],
	"Wires":[],
	"Displays": None
}

ID = 0
InputsY = 0

# 10 8-bit lines for microinstructions, 256 instructions
for instruc in range(numInstructions):
	for microinstruc in range(numMicroinstructionLines):
		JSON["InputPins"].append({
			"Name": "IN",
			"ID": ID,
			"Position": {
				"x": 0,
				"y": InputsY
			},
			"BitCount": 8,
			"Colour": 0,
			"ValueDisplayMode": 1
		})
		ID += 1
		JSON["OutputPins"].append({
			"Name": "OUT",
			"ID": ID,
			"Position": {
				"x": 200,
				"y": InputsY
			},
			"BitCount": 8,
			"Colour": 0,
			"ValueDisplayMode": 0
		})
		InputsY += 0.5
		ID += 1
		JSON["Wires"].append({
			"SourcePinAddress": {
				"PinID": 0,
				"PinOwnerID": (instruc*numMicroinstructionLines + microinstruc)*2
			},
			"TargetPinAddress": {
				"PinID": 0,
				"PinOwnerID": (microinstruc*numInstructions + instruc)*2+1
			},
			"ConnectionType": 0,
			"ConnectedWireIndex": -1,
			"ConnectedWireSegmentIndex": -1,
			"Points": [{"x": 0.0, "y": 0.0}, {"x": 0.0, "y": 0.0}]
	})

with open("D:/DigitalLogicSim/python/8-Bit-CPU/INS_ROM/JSON/INS-ROM_WEAVER.json", "w", encoding="utf-8") as file:
	file.write(json.dumps(JSON).encode().decode('unicode-escape'))