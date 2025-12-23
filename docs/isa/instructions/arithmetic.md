# Arithmetic Instructions

## ADD &mdash; Add

### Syntax
```asm
ADD dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; dst + src

### Flags affected
ZF, CF, OF, PF

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x07   |
| register | register | 0x08   |
| register | mem addr | 0x09   |
| mem addr | immediate| 0x0A   |
| mem addr | register | 0x0B   |
| mem addr | mem addr | 0x0C   |

## SUB &mdash; Subtract

### Syntax
```asm
SUB dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; dst - src

### Flags affected
ZF, CF, SF, OF, PF

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x0D   |
| register | register | 0x0E   |
| register | mem addr | 0x0F   |
| mem addr | immediate| 0x10   |
| mem addr | register | 0x11   |
| mem addr | mem addr | 0x12   |



## MUL &mdash; Multiply

### Syntax
```asm
MUL dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; dst * src

### Flags affected
ZF, CF, PF

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x13   |
| register | register | 0x14   |
| register | mem addr | 0x15   |
| mem addr | immediate| 0x16   |
| mem addr | register | 0x17   |
| mem addr | mem addr | 0x18   |

## DIV &mdash; Divide

### Syntax
```asm
DIV dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; dst / src

### Flags affected
ZF

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x19   |
| register | register | 0x1A   |
| register | mem addr | 0x1B   |
| mem addr | immediate| 0x1C   |
| mem addr | register | 0x1D   |
| mem addr | mem addr | 0x1E   |