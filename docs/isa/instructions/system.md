# System Instructions

## NOP &mdash; No Operation

### Syntax
```asm
NOP
```

### Argument Types
None

### Operation
None

### Flags affected
None

### Encoding
| Opcode |
|--------|
| 0x00   |



## HLT &mdash; Halt

### Syntax
```asm
HLT
```

### Argument Types
None

### Operation
Ends program execution until chip restart

### Flags affected
None

### Encoding
| Opcode |
|--------|
| 0xFF   |



## PAGE &mdash; Page

### Description
**Sets the PAGE register**  
Allows access to more sections of memory. There are 256 pages, each with 256 addressable bytes.  

The value stored in the PAGE register is prepended to any addressed memory location. 

### Syntax
```asm
PAGE pg
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| pg  | &cross;        | &check;  | &check;   |

### Operation
PAGE register &larr; pg

### Flags affected
None

### Encoding
| pg type   | Opcode |
|-----------|--------|
| immediate | 0x67   |
| register  | 0x68   |