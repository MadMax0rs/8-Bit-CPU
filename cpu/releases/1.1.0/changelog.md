



# Halting
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

<br><br>

# Paging

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

<br><br>

# I/O

## Input

### Syntax
```asm
IN inPin, dst
```

### Argument Types
| Arg  | Memory address | Register | Immediate |
|------|----------------|----------|-----------|
| inPin| &cross;        | &check;  | &cross;   |
| dst  | &cross;        | &check;  | &cross;   |

### Operation
dst &larr; inPin

### Flags affected
None

### Encoding
| dst type | inPin type | Opcode |
|----------|------------|--------|
| register | register   | 0x69   |

## Output
### Syntax
```asm
MOV dst, src
```
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| src | &check;        | &check;  | &check;   |
| dst | &cross;        | &check;  | &cross;   |

### Examples
- Added `io` example

