````asm
// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.


// Set R2 to 0 
@R2
M=0

// Check for zeros
@R0
D=M
@END
D;JEQ
@R1
D=M
@END
D;JEQ 

// Set iterator

@R0
D=M
@i
M=D

// Loop thru addition
(LOOP)
@R1
D=M
@R2
M=D+M
@i
M=M-1
D=M
@END
D;JEQ
@LOOP
0;JMP

(END)
0;JMP

````
