; This is a random string generator
; Generates random string of Length L, containing all capital letters
; A test program will call this procedure 20 times and display the strings in the console window. The string size will be preset as a constant
; Author: Eric Tallant
; Date: 06/26/2019


include Irvine32.inc
.data
source BYTE "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
randString BYTE 25 DUP(?), 0
prompt BYTE "Press any key to continue....", 0

.code
main proc
mov ecx, sizeof randString - 1     ; loop sizeof source - 1 times
mov esi, 0                         ; index for the randString
L:
mov eax sizeof source - 1       
call randomRange                   ; generate a random index with range form 0 to sizeof source - 2 and store in eax

mov bl, source[eax]                ; copy the char at index position to a position in randString
mov randString[esi], bl
INC esi                            ; increment esi by 1
loop L

mov edx, OFFSET randString         ; print out the random string 
call WriteString
mov edx, OFFSET prompt             ; hold screen to display result
call WriteString
call ReadChar

exit
main endp
end main
