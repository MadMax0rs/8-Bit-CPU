# Status Flags

## Flags
| Flag | Name     | Description |
|------|----------|-------------|
| ZF   | Zero     | Set if result = 0|
| CF   | Carry    | Set if unsigned overflow occurred|
| SF   | Sign     | Set if last calculation was negative (only during subtraction)|
| OF   | Overflow | Set if signed overflow occurred|
| PF   | Parity   | Set if there is an even number of set bits in the result|

## Flag register layout
| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|-----|---|---|---|---|---|---|---|---|
| Flag| 0 | 0 | 0 | PF| OF| SF| CF| ZF|