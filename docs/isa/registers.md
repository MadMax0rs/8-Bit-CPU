# Registers


## General-purpose registers
| Name | Width | Description|
|------|-------|------------|
| R0   | 8     | General-purpose|
| R1   | 8     | General-purpose|
| R2   | 8     | General-purpose|
| R3   | 8     | General-purpose|
| R4   | 8     | General-purpose|
| R5   | 8     | General-purpose|
| R6   | 8     | General-purpose|

## Special registers (inaccessable)

| Name | Width          | Description|
|------|----------------|----------------------|
| IP   | 8              | Instruction Pointer  |
| SP   | 8              | Stack Pointer        |
| FLAGS| 8 (only uses 5)| Status Flags Register|

## Output registers (write only)
| Name | Width | Description |
|------|-------|-------------|
| P0   | 8     | Output      |
| P1   | 8     | Output      |
| P2   | 8     | Output      |
| P3   | 8     | Output      |

## Input Registers (read only)
These registers can only be used with the `IN` instruction as the `inPin` argument
| Name | Width | Description |
|------|-------|-------------|
| I0   | 8     | Input       |
| I1   | 8     | Input       |
| I2   | 8     | Input       |
| I3   | 8     | Input       |

## Reset state
- PC = 0x00
- SP = 0x00
- FLAGS = NOT RESET
