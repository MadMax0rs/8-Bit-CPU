# Control Flow Instructions



## JMP &mdash; Unconditional Jump

### Description
None

### Aliases
None

### Syntax
```asm
JMP addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr

### Flags used
None

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x45   |
| register  | 0x46   |



## JZ &mdash; Jump if Zero

### Description
None

### Aliases
- JE &mdash; Jump if Equal

### Syntax
```asm
JZ addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if ZF

### Flags used
ZF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x47   |
| register  | 0x48   |



## JNZ &mdash; Jump if Not Zero

### Description
None

### Aliases
- JNE &mdash; Jump if Not Equal

### Syntax
```asm
JNZ addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if !ZF

### Flags used
ZF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x49   |
| register  | 0x4A   |



## JS &mdash; Jump if Sign

### Description
None

### Aliases
None

### Syntax
```asm
JS addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if SF

### Flags used
SF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x4B   |
| register  | 0x4C   |



## JNS &mdash; Jump if Not Sign

### Description
None

### Aliases
None

### Syntax
```asm
JNS addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if !SF

### Flags used
SF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x4D   |
| register  | 0x4E   |



## JG &mdash; Jump if Greater

### Description
signed greater than

### Aliases
- JNLE &mdash; Jump if Not Less than or Equal to

### Syntax
```asm
JG addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if !ZF && !(SF^OF)

### Flags used
ZF, SF, OF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x4F   |
| register  | 0x50   |



## JGE &mdash; Jump if Greater than or Equal to

### Description
signed greater than or equal to

### Aliases
- JNL &mdash; Jump if Not Less than

### Syntax
```asm
JGE addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if !(SF^OF)

### Flags used
SF, OF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x51   |
| register  | 0x52   |



## JL &mdash; Jump if Less than

### Description
signed less than

### Aliases
- JNGE &mdash; Jump if Not Greater than or Equal to

### Syntax
```asm
JL addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if SF^OF

### Flags used
SF, OF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x53   |
| register  | 0x54   |



## JLE &mdash; Jump if Less than or Equal to

### Description
signed less than or equal to

### Aliases
- JNG &mdash; Jump if Not Greater than

### Syntax
```asm
JLE addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if ZF && !(SF^OF)

### Flags used
ZF, SF, OF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x55   |
| register  | 0x56   |



## JA &mdash; Jump if Above

### Description
unsigned greater than

### Aliases
- JNBE &mdash; Jump if Not Below or Equal to

### Syntax
```asm
JA addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if !ZF && !CF

### Flags used
ZF, CF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x57   |
| register  | 0x58   |



## JAE &mdash; Jump if Above or Equal to

### Description
unsigned greater than or equal to

### Aliases
- JNB &mdash; Jump if Not Below
- JNC &mdash; Jump if Not Carry

### Syntax
```asm
JAE addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if !CF

### Flags used
CF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x59   |
| register  | 0x5A   |



## JB &mdash; Jump if Above or Equal to

### Description
unsigned greater than or equal to

### Aliases
- JNAE &mdash; Jump if Not Above or Equal to
- JC &mdash; Jump if Carry

### Syntax
```asm
JB addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if CF

### Flags used
CF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x5B   |
| register  | 0x5C   |



## JBE &mdash; Jump if Below or Equal to

### Description
unsigned greater than or equal to

### Aliases
- JNA &mdash; Jump if Not Above

### Syntax
```asm
JBE addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if ZF || CF

### Flags used
ZF, CF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x5D   |
| register  | 0x5E   |



## JP &mdash; Jump if Above or Equal to

### Description
Jump if the last result contained an even number of set bits 

### Aliases
- JPE &mdash; Jump if Parity Even

### Syntax
```asm
JP addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if PF

### Flags used
PF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x5F   |
| register  | 0x60   |



## JNP &mdash; Jump if Not Parity

### Description
Jump if the last result contained an odd number of set bits

### Aliases
- JPO &mdash; Jump if Parity Odd

### Syntax
```asm
JNP addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if !PF

### Flags used
PF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x61   |
| register  | 0x62   |



## JO &mdash; Jump if Overflow

### Description
Jump if the last result overflowed

### Aliases
None

### Syntax
```asm
JO addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if OF

### Flags used
OF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x63   |
| register  | 0x64   |



## JNO &mdash; Jump if Not Overflow

### Description
Jump if the last result did not overflow

### Aliases
- JPO &mdash; Jump if Parity Odd

### Syntax
```asm
JNO addr
```

### Argument Types
| Arg | Memory address | Register | Immediate |
|-----|----------------|----------|-----------|
| addr| &cross;        | &check;  | &check;   |

### Operation
IP &larr; addr if !OF

### Flags used
OF

### Encoding
| addr type | Opcode |
|-----------|--------|
| immediate | 0x65   |
| register  | 0x66   |