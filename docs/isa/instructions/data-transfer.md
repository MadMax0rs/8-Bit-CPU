# Data Transfer Instructions


## MOV &mdash; Move

### Syntax
```asm
MOV dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; src

### Flags affected
None

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x01   |
| register | register | 0x02   |
| register | mem addr | 0x03   |
| mem addr | immediate| 0x04   |
| mem addr | register | 0x05   |
| mem addr | mem addr | 0x06   |


## PUSH &mdash; Push

### Syntax
```asm
push src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |

### Operation
[SP - 1] &larr; src

### Flags affected
None

### Encoding
| src type | Opcode |
|----------|--------|
| immediate| 0x1F   |
| register | 0x20   |
| mem addr | 0x21   |


## POP &mdash; Pop

### Syntax
```asm
pop dst
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| dst | &check;        | &check;  | &cross;   |

### Operation
dst &larr; [SP]

### Flags affected
None

### Encoding
| src type | Opcode |
|----------|--------|
| register | 0x22   |
| mem addr | 0x23   |


## XCHG &mdash; Exchange

### Syntax
```asm
XCHG dst, src
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src1| &check;        | &check;  | &cross;   |
| src2| &check;        | &check;  | &cross;   |

### Operation
TEMP &larr; src1  
src1 &larr; src2  
src2 &larr; TEMP  
**aka**  
src1 &harr; src2

### Flags affected
None

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | register | 0x42   |
| register | mem addr | 0x43   |
| mem addr | mem addr | 0x44   |