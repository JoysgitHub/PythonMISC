#SIMPLE WORD GUESSER GAME WIRTTEN IN PYTHON
import random

word_list = ["PROGRAMMING", "SOFTWARE", "HARDWARE", "DATABASE", "ALGORITHM", 
"NETWORK", "CYBERSECURITY", "PYTHON", "JAVASCRIPT", "LINUX",
"OPERATING", "PERIPHERAL", "INTERFACE", "VIRTUALIZATION", "DEBUGGING",
 "COMPILER", "FIRMWARE", "CRYPTOGRAPHY", "CACHE", "FLOPPY","HACKATHON", "RANSOMWARE", "BIOMETRICS", 
 "FIBEROPTIC", "TELECOMM", "CRYPTOCURRENCY", "SUPERCOMPUTER", "INTERNET", "MALWARE"]

word = random.choice(word_list)

fullWord = list(word)
missingWord = list(word)
for i in range(4):
    index = random.randint(0,len(fullWord)-1)
    missingWord[index] = "_"

chances = 5
print("-"*20)
print(" ".join(missingWord))

for m in range(chances):
    choice =   input("> ")
    for i in range(len(fullWord)):
            if fullWord[i] == choice.upper():
                missingWord[i] = fullWord[i]
    print("-"*20)
    print(' '.join(missingWord))
    if "_" not in missingWord:
        print("YOU WIN")
        break            
    chances -=1
    print(f"{chances} chances left")
if "_" in missingWord:
    print("YOU LOOSE")
print(f"Word: {word}")





