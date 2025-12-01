# Notes
# Password
# Dial with numbers 0 through 99
# Document with sequence of rotations
# L or R which indicates left or right (Higher, lower)
# Distance value
# If the dial was at 11 and input was R8 it would move to 19
# If at 99 and input R1 = 0
# The dial starts at 50
# Decoy, the actual password is the number of times the dial is pointing at 0
# after any rotation in the sequence 
# (Basically just += 1 a var for password each time it stops at 0 then?)

puzzleInputs = []


with open("day01\puzzle_input.txt") as puzzle:
    for x in puzzle:
        puzzleInputs.append(x.replace("\n", ""))
        
def password_cracker(inputs: list) -> int:
    password = 0
    dial = 50
    
    for s in inputs:
        direction = s[0]
        num = int(s[1:])
        
        if direction == "L":
            dial -= num
        elif direction == "R":
            dial += num
        
        dial = dial % 100
        
        if dial == 0:
            password += 1
    
    return password

print(password_cracker(puzzleInputs))