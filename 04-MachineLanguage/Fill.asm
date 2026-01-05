// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// Detect key
(KBDLOOP)
@KBD
D=M
@BLKSCREEN // Black if pressed
D;JGT
@WHTSCREEN // White if not presssed
D;JEQ
@KBDLOOP
0;JMP

(BLKSCREEN)
// Iterator
@8192
D=A
@i
M=D

(BLOOP)
@SCREEN
A=D+A
M=-1

@i
M=M-1
D=M
@BLOOP
D;JGE
@KBDLOOP
0;JMP

(WHTSCREEN)
// Iterator
@8192
D=A
@i
M=D

(WLOOP)
@SCREEN
A=D+A
M=0

@i
M=M-1
D=M
@WLOOP
D;JGE
@KBDLOOP
0;JMP


