
#SIMPLE WORD GUESSER GAME WIRTTEN IN PYTHON
#REQIRES "words.txt" to function
import random

with open("words.txt", "r") as file:
    words = file.read().splitlines()

word = random.choice(words)

fullWord = list(word)
missingWord = list(word)
for i in range(4):
    index = random.randint(0,len(fullWord)-1)
    missingWord[index] = "_"

chances = 5
print("-"*20)
print(" ".join(missingWord))

for m in range(chances):
    # system('cls')
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




