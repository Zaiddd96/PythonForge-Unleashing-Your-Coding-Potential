import random

player_score = 0
computer_score = 0

print("𝕮𝖗𝖎𝖈𝕶𝖊𝖙 𝕾𝖍𝖔𝖜𝖉𝖔𝖜𝖓")

def play_batting():
    global player_score
    while True:
        player_run = int(input("Play a number: "))
        computer_ball = random.randint(1, 6)
        print(f"Computer's ball: {computer_ball}")
        if player_run == computer_ball:
            print("Out!")
            break
        else:
            player_score += player_run
            continue

    print(f"Your Score: {player_score} runs!")

def play_bowling():
    while True:
        global computer_score
        computer_bat = random.randint(1, 6)
        player_ball = int(input("Bowling: "))
        print(f"Computer plays: {computer_bat}")
        if computer_bat == player_ball:
            print("Out!")
            break
        else:
            computer_score += computer_bat
            continue

    print(f"Computer Scores {computer_score} runs!")

def determine_winner():
    global player_score
    global computer_score
    if player_score > computer_score:
        print("You won the Match!")
    elif player_score == computer_score:
        print("The Match is a Draw!")
    else:
        print("You lost the Match!")

toss = random.randint(1, 6)
while True:
    try:
        choice = input("Odd or Even? ").lower()
        if choice == "odd":
            break
        elif choice == "even":
            break
        else:
            print("Please enter 'odd' or 'even!'")
    except ValueError:
        print("Invalid Input. Please Enter a valid Characters!")
        
        

while True:
    try:
        player_play = int(input("Play a number (1-6): "))
        if 1 <= player_play <= 6:
            break
        else:
            print("Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"You chose {player_play}")
print(f"Computer plays: {toss}")

if (toss + player_play) % 2 != 0:
    result = "odd"
else:
    result = "even"

if choice == result:
    toss_winner = input("You won the toss! Batting or Bowling? ").lower()
    print(f"You choose to {toss_winner}")
    if toss_winner == "bat":
        play_batting()
        print("Innings over!")
        print("You are Bowling now!")
        play_bowling()
    else:
        play_bowling()
        print("Innings over!\n")
        print("You are Batting now!")
        play_batting()
else:
    print("You lost the toss. Computer will decide.")
    computer_choice = random.choice(["bat", "bowl"])
    print(f"Computer chooses to {computer_choice}")
    if computer_choice == "bat":
        play_bowling()
        print("Innings over!")
        print("You are Bowling now!")
        play_batting()
    else:
        play_batting()
        print("Innings over!\n")
        print("Computer is Bowling now!")
        play_bowling()

determine_winner()





