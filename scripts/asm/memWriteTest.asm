; Index to calculate
mov reg2, 10



mov reg0, 0
mov reg1, 1

; Addr: 0x09
loop:
cmp reg2, 0
je exit

add reg0, reg1
; Make reg1 the big one again
xchg reg0, reg1
sub reg2, 1; dec reg2
jmp loop

; Addr: 26
exit:
; Output
mov [0x24], reg0