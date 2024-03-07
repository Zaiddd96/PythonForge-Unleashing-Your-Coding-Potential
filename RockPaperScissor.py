#Rock paper scissor!
import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
rps = [rock,paper,scissor]
user = int(input("Choose 0 for Rock, 1 for paper, 2 for scissor: \n"))
if user >= 3 or user < 0:
    print("Invalid input! Try again.")
else:
    print(rps[user])
    computer = random.randint(0,2)
    print("Computer choose!")
    print(rps[computer])
    if user == computer:
        print("Draw")
    elif user == 2 and computer == 0:
        print("You Lose!")
    elif computer == 0 and user == 2:
        print("You win!")
    elif user > computer:
        print("You win!")
    elif user < computer:
        print("You lose!")