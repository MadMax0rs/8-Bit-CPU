# Comparison Instructions


## CMP &mdash; Compare

### Syntax
```asm
CMP src1, src2
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src1| &check;        | &check;  | &check;   |
| src2| &check;        | &check;  | &cross;   |

### Operation
FLAGS &larr; src1 - src1

### Flags affected
ZF, CF, SF, OF, PF

### Encoding
| dst type | src type | Opcode |
|----------|----------|--------|
| register | immediate| 0x34   |
| register | register | 0x35   |
| register | mem addr | 0x36   |
| mem addr | immediate| 0x37   |
| mem addr | register | 0x38   |
| mem addr | mem addr | 0x39   |