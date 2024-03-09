import random
from ListOfWords import words
from artt import *

print(logo)
choice = random.choice(words)
display = []
for letter in choice:
    display += "_"

lives = 6

end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already Guessed {guess}.")
    for i in range(len(choice)):
        if guess == choice[i]:
            display[i] = choice[i]

    
    if guess not in choice:
        print(f"You Guessed letter {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            print("You Loose!")
            print(f"The answer is {choice}")
            end_game = True
        
    print(f"{' '.join(display)}")

    if '_' not in display:
        print("You Won!")
        end_game = True

    print(stages[lives])
    
        

    
