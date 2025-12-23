# Opcode Map

| Opcode | Mnemonic | Argument(s) | Category     | Aliases |
|--------|----------|-------------|--------------|---------|
| 0x00   | NOP      |             | System       |         |
| 0x01   | MOV      | reg,imm     | Data Transfer|         |
| 0x02   | MOV      | reg,reg     | Data Transfer|         |
| 0x03   | MOV      | reg,mem     | Data Transfer|         |
| 0x04   | MOV      | mem,imm     | Data Transfer|         |
| 0x05   | MOV      | mem,reg     | Data Transfer|         |
| 0x06   | MOV      | mem,mem     | Data Transfer|         |
| 0x07   | ADD      | reg,imm     | Arithmetic   |         |
| 0x08   | ADD      | reg,reg     | Arithmetic   |         |
| 0x09   | ADD      | reg,mem     | Arithmetic   |         |
| 0x0A   | ADD      | mem,imm     | Arithmetic   |         |
| 0x0B   | ADD      | mem,reg     | Arithmetic   |         |
| 0x0C   | ADD      | mem,mem     | Arithmetic   |         |
| 0x0D   | SUB      | reg,imm     | Arithmetic   |         |
| 0x0E   | SUB      | reg,reg     | Arithmetic   |         |
| 0x0F   | SUB      | reg,mem     | Arithmetic   |         |
| 0x10   | SUB      | mem,imm     | Arithmetic   |         |
| 0x11   | SUB      | mem,reg     | Arithmetic   |         |
| 0x12   | SUB      | mem,mem     | Arithmetic   |         |
| 0x13   | MUL      | reg,imm     | Arithmetic   |         |
| 0x14   | MUL      | reg,reg     | Arithmetic   |         |
| 0x15   | MUL      | reg,mem     | Arithmetic   |         |
| 0x16   | MUL      | mem,imm     | Arithmetic   |         |
| 0x17   | MUL      | mem,reg     | Arithmetic   |         |
| 0x18   | MUL      | mem,mem     | Arithmetic   |         |
| 0x19   | DIV      | reg,imm     | Arithmetic   |         |
| 0x1A   | DIV      | reg,reg     | Arithmetic   |         |
| 0x1B   | DIV      | reg,mem     | Arithmetic   |         |
| 0x1C   | DIV      | mem,imm     | Arithmetic   |         |
| 0x1D   | DIV      | mem,reg     | Arithmetic   |         |
| 0x1E   | DIV      | mem,mem     | Arithmetic   |         |
| 0x1F   | PUSH     | imm         | Data Transfer|         |
| 0x20   | PUSH     | reg         | Data Transfer|         |
| 0x21   | PUSH     | mem         | Data Transfer|         |
| 0x22   | POP      | reg         | Data Transfer|         |
| 0x23   | POP      | mem         | Data Transfer|         |
| 0x24   | SHL      | reg,imm     | Logical      |         |
| 0x25   | SHL      | reg,reg     | Logical      |         |
| 0x26   | SHR      | reg,imm     | Logical      |         |
| 0x27   | SHR      | mem,reg     | Logical      |         |
| 0x28   | AND      | reg,imm     | Logical      |         |
| 0x29   | AND      | reg,reg     | Logical      |         |
| 0x2A   | AND      | reg,mem     | Logical      |         |
| 0x2B   | AND      | mem,imm     | Logical      |         |
| 0x2C   | AND      | mem,reg     | Logical      |         |
| 0x2D   | AND      | mem,mem     | Logical      |         |
| 0x2E   | OR       | reg,imm     | Logical      |         |
| 0x2F   | OR       | reg,reg     | Logical      |         |
| 0x30   | OR       | reg,mem     | Logical      |         |
| 0x31   | OR       | mem,imm     | Logical      |         |
| 0x32   | OR       | mem,reg     | Logical      |         |
| 0x33   | OR       | mem,mem     | Logical      |         |
| 0x34   | XOR      | reg,imm     | Logical      |         |
| 0x35   | XOR      | reg,reg     | Logical      |         |
| 0x36   | XOR      | reg,mem     | Logical      |         |
| 0x37   | XOR      | mem,imm     | Logical      |         |
| 0x38   | XOR      | mem,reg     | Logical      |         |
| 0x39   | XOR      | mem,mem     | Logical      |         |
| 0x3A   | NOT      | reg         | Logical      |         |
| 0x3B   | NOT      | mem         | Logical      |         |
| 0x3C   | CMP      | reg,imm     | Compare      |         |
| 0x3D   | CMP      | reg,reg     | Compare      |         |
| 0x3E   | CMP      | reg,mem     | Compare      |         |
| 0x3F   | CMP      | mem,imm     | Compare      |         |
| 0x40   | CMP      | mem,reg     | Compare      |         |
| 0x41   | CMP      | mem,mem     | Compare      |         |
| 0x42   | XCHG     | reg, reg    | Data Transfer|         |
| 0x43   | XCHG     | reg, mem    | Data Transfer|         |
| 0x44   | XCHG     | mem, mem    | Data Transfer|         |
| 0x45   | JMP      | imm         | Control Flow |         |
| 0x46   | JMP      | reg         | Control Flow |         |
| 0x47   | JZ       | imm         | Control Flow | JE      |
| 0x48   | JZ       | reg         | Control Flow | JE      |
| 0x49   | JNZ      | imm         | Control Flow | JNE     |
| 0x4A   | JNZ      | reg         | Control Flow | JNE     |
| 0x4B   | JS       | imm         | Control Flow |         |
| 0x4C   | JS       | reg         | Control Flow |         |
| 0x4D   | JNS      | imm         | Control Flow |         |
| 0x4E   | JNS      | reg         | Control Flow |         |
| 0x4F   | JG       | imm         | Control Flow | JNLE    |
| 0x50   | JG       | reg         | Control Flow | JNLE    |
| 0x51   | JGE      | imm         | Control Flow | JNL     |
| 0x52   | JGE      | reg         | Control Flow | JNL     |
| 0x53   | JL       | imm         | Control Flow | JNGE    |
| 0x54   | JL       | reg         | Control Flow | JNGE    |
| 0x55   | JLE      | imm         | Control Flow | JNG     |
| 0x56   | JLE      | reg         | Control Flow | JNG     |
| 0x57   | JA       | imm         | Control Flow | JNBE    |
| 0x58   | JA       | reg         | Control Flow | JNBE    |
| 0x59   | JAE      | imm         | Control Flow | JNB, JNC|
| 0x5A   | JAE      | reg         | Control Flow | JNB, JNC|
| 0x5B   | JB       | imm         | Control Flow | JNAE, JC|
| 0x5C   | JB       | reg         | Control Flow | JNAE, JC|
| 0x5D   | JBE      | imm         | Control Flow | JNA     |
| 0x5E   | JBE      | reg         | Control Flow | JNA     |
| 0x5F   | JP       | imm         | Control Flow | JPE     |
| 0x60   | JP       | reg         | Control Flow | JPE     |
| 0x61   | JNP      | imm         | Control Flow | JPO     |
| 0x62   | JNP      | reg         | Control Flow | JPO     |
| 0x63   | JO       | imm         | Control Flow |         |
| 0x64   | JO       | reg         | Control Flow |         |
| 0x65   | JNO      | imm         | Control Flow |         |
| 0x66   | JNO      | reg         | Control Flow |         |