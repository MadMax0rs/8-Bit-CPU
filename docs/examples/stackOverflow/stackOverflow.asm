; Index to calculate

mov r0, 0x00

loop:
	push r0
	add r0, 0x01
	jmp loop
