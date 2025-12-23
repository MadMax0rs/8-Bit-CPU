# Addressing Modes

**Purpose:** How operands are interpreted

## Immediate
Immediates can be in decimal, hex, or binary, as long as they have the following prefix

| Base | Prefix | Example | Decimal Representation | Max Value |
|------|--------|---------|------------------------|-----------|
| 10   | None   | 132     | 132                    | 255       |
| 16   | 0x     | 0x3E    | 62                     | 0xFF      |
| 2    | 0b     | 0b100101| 37                     | 0b11111111|

### Example
```asm
; All do the same thing, just with the immediate value represented in a different base
add r0, 49
add r0, 0x31
add r0, 0b110001
```

## Memory direct
- Represents an address in memory
- Just an immediate value wrapped in []

### Example
```asm
; All do the same thing, just with the memory address represented in a different base
add [49], r0
add [0x31], r0
add [0b110001], r0
```