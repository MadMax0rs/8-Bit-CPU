import json

#Chip name: 8x32-1x256

JSON = {
	"DLSVersion": "2.1.6",
	"Name": "8x32-1x256",
	"NameLocation": 0,
	"ChipType": 0,
	"Size": {
		"x": 1.775,
		"y": 64.0
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
	"Wires": [],
	"Displays": None
}

ID = 0
yOutputs = 0.0
yInputs = 0.0
ySubChips = 0.0

for x in range(32):
	for y in range(8):
		JSON["OutputPins"].append({
			"Name": x * 8 + y,
			"ID": ID,
			"Position": {
				"x": 8,
				"y": yOutputs
			},
			"BitCount": 1,
			"Colour": 0,
			"ValueDisplayMode": 0
		})
		ID += 1
		yOutputs+=0.5
	JSON["InputPins"].append({
		"Name": "IN",
		"ID": ID,
		"Position": {
			"x": 0,
			"y": yInputs
		},
		"BitCount": 8,
		"Colour": 0,
		"ValueDisplayMode": 1
	})
	ID += 1
	yInputs+=0.5
	
	JSON["SubChips"].append({
		"Name":"8-1BIT",
		"ID":ID,
		"Label":"",
		"Position":{
			"x":4,
			"y":ySubChips
		},
		"OutputPinColourInfo":[{"PinColour":0,"PinID":1},{"PinColour":0,"PinID":2},{"PinColour":0,"PinID":3},{"PinColour":0,"PinID":4},{"PinColour":0,"PinID":5},{"PinColour":0,"PinID":6},{"PinColour":0,"PinID":7},{"PinColour":0,"PinID":8}],
		"InternalData": None
	})
	ID += 1
	ySubChips += 4.0

	for i in range(8):
		JSON["Wires"].append({
			"SourcePinAddress":{
				# i goes from 0-7, want it to go from 1-8, 8-0=8, 8-7=1, 
				"PinID": 8 - i,	 # The input pin is 0, the output pins are 1(H), 2(G), 3(F), 4(E), 5(D), 6(C), 7(B), 8(A)
				"PinOwnerID":ID - 1
			},
			"TargetPinAddress":{
				"PinID":0,
				"PinOwnerID":x*10+i
			},
			"ConnectionType":0,
			"ConnectedWireIndex":-1,
			"ConnectedWireSegmentIndex":-1,
			"Points":[{"x":0.0,"y":0.0},{"x":0.0,"y":0.0}]
		})
		
	JSON["Wires"].append({
		"SourcePinAddress":{
			"PinID":0,
			"PinOwnerID":ID - 2
		},
		"TargetPinAddress":{
			"PinID":0,
			"PinOwnerID":ID - 1
		},
		"ConnectionType":0,
		"ConnectedWireIndex":-1,
		"ConnectedWireSegmentIndex":-1,
		"Points":[{"x":0.0,"y":0.0},{"x":0.0,"y":0.0}]
	})

with open(f"D:\DigitalLogicSim\python\8-Bit-CPU\INS_ROM\8x32-1x256.json", "w", encoding="utf-8") as file:
	file.write(json.dumps(JSON).encode().decode('unicode-escape'))