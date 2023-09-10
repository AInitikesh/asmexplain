.data
value: .quad 0x1234567890abcdef

.text
.global main
main:
    ldr x0, =value

    ldrb w1, [x0]; /* /* Hello 
    Goood
    How are you */ ldrh w2, [x0]
    ldr  w3, [x0]
    
    ldrsb w4, [x0] // Great comment
    ldrsh w5, [x0]
    ldrsw x6, [x0]

    mov x0, #0
    ret