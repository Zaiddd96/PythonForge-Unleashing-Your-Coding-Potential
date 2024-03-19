#Guess The Number
from random import randint
from artt import GuessTheNUmber
EASY = 10
HARD = 5
def choice():
    level = input("Choose the level of difficulty easy and hard: ").lower()
    if level == "easy":
        return EASY
    else:
        return HARD

def Answer(guess,random_guess):
    if guess > random_guess: print("Too High!\nGuess again")
    elif guess < random_guess: print("Too low!\nGuess again")
    else: print(f"You got it! The number was {random_guess}")

def GuessingTheNumber():
    print(GuessTheNUmber)
    print("Welcome to the Guess Quest!")
    print("Guess a number between 1-100!")
    random_num = randint(1,101)
    attempts = choice()
    print(f"You have {attempts} turns left!")
    guessed = 0
    while guessed != random_num:
        guessed = int(input("Guess a number: "))
        Answer(guess=guessed,random_guess=random_num)
        attempts -= 1
        if attempts == 0:
            print(f"Game over! You lost all your turns!\nThe number was {random_num}")
            return
        else: print(f"You have {attempts} turns left!")


GuessingTheNumber()