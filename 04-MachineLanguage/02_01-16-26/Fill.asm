// Completed 1.16.26

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// Screen address: 16384, size: 8192k, keyboard address: 24576

(LOOP)
// Set iterator for screen addressing
@8192
D=A
@i
M=D

// Monitor key press
@KBD
D=M
@BLOOP
D;JGT
@WLOOP
0;JMP

// Turn screen black
(BLOOP)
@i
D=M
@SCREEN
A=D+A
M=-1
@i
M=M-1
D=M
@LOOP
D;JLT
@BLOOP
0;JMP

// Turn screen white
(WLOOP)
@i
D=M
@SCREEN
A=D+A
M=0
@i
M=M-1
D=M
@LOOP
D;JLT
@WLOOP
0;JMP

