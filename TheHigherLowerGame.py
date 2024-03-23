from test import data
import random
from artt import *
from replit import clear

def Questions():
    """Get data from random account"""
    ques = random.choice(data)
    print(f"{ques['name']}, a {ques['description']}, from {ques['country']}")
    return ques

def CompareFollowers(guess,a,b):
    """Checks followers against user's guess 
    and returns '1' or '2' if they got it right.
        Or '0' if they got it wrong.""" 
    if "a" in guess and a['follower_count'] >= b['follower_count']:
        return 1
    elif "b" in guess and b['follower_count'] >= a['follower_count']:
        return 2
    else: 
        return 0

def HigherLower():
    """The main Higher-Lower game!"""
    print(HigherLower)
    game_should_continue = False
    score = 0
    Question_A = Questions()
    while not game_should_continue:
        print(Vs)
        Question_B = Questions()
        while True:
            player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if player_guess == "a" or player_guess == "b": break
            else:
                print("Please enter 'A' or 'B'")    
         
        compare = CompareFollowers(guess=player_guess,a=Question_A,b=Question_B)
        clear()
        print(HigherLower)
        if compare == 1:
            score += 1
            print("Correct! Your score is now ", score)
            Question_A = Question_B
            print(f"{Question_B['name']}, a {Question_B['description']}, from {Question_B['country']}")

        elif compare == 2:
            score += 1
            print(f"You're right! Current score: {score}.")
            Question_A = Question_B
            print(f"{Question_A['name']}, a {Question_A['description']}, from {Question_A['country']}")
        else:
            game_should_continue = True
            print(f"Sorry, that's wrong. Final score: {score}")

HigherLower()









