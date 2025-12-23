# Logical Instructions



## SHL &mdash; Shift Left

### Syntax
```asm
SHL src, amount
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &cross;        | &check;  | &cross;   |
| amount| &cross;      | &check;  | &check;   |

### Operation
src &larr; src << amount

### Flags affected
ZF, PF

### Encoding
| src type | amount type | Opcode |
|----------|-------------|--------|
| register | immediate   | 0x24   |
| register | register    | 0x25   |



## SHR &mdash; Shift Right

### Syntax
```asm
SHR src, amount
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &cross;        | &check;  | &cross;   |
| amount| &cross;      | &check;  | &check;   |

### Operation
src &larr; src >> amount

### Flags affected
ZF, PF

### Encoding
| src type | amount type | Opcode |
|----------|-------------|--------|
| register | immediate   | 0x26   |
| register | register    | 0x27   |



## AND &mdash; Bitwise And

### Syntax
```asm
AND dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; dst & src

### Flags affected
ZF, PF

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x28   |
| register | register | 0x29   |
| register | mem addr | 0x2A   |
| mem addr | immediate| 0x2B   |
| mem addr | register | 0x2C   |
| mem addr | mem addr | 0x2D   |



## OR &mdash; Bitwise Or

### Syntax
```asm
OR dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; dst | src

### Flags affected
ZF, PF

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x2E   |
| register | register | 0x2F   |
| register | mem addr | 0x30   |
| mem addr | immediate| 0x31   |
| mem addr | register | 0x32   |
| mem addr | mem addr | 0x33   |



## XOR &mdash; Bitwise Xor

### Syntax
```asm
XOR dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; dst ^ src

### Flags affected
ZF, PF

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x34   |
| register | register | 0x35   |
| register | mem addr | 0x36   |
| mem addr | immediate| 0x37   |
| mem addr | register | 0x38   |
| mem addr | mem addr | 0x39   |



## NOT &mdash; Bitwise Not

### Syntax
```asm
NOT src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &cross;   |

### Operation
src &larr; !src

### Flags affected
ZF, PF

### Encoding
| src type | Opcode |
|----------|--------|
| register | 0x3A   |
| mem addr | 0x3B   |