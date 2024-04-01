import random
import os

deck = {
    11: '''
┌───────┐
│A      │
│       │
│   ♠   │
│       │
│      A│
└───────┘
    ''',
    2: '''
┌───────┐
│2      │
│   ♦   │
│       │
│   ♦   │
│      2│
└───────┘
    ''',
    3: '''
┌───────┐
│3      │
│   ♥   │
│   ♥   │
│   ♥   │
│      3│
└───────┘
    ''',
    4: '''
┌───────┐
│4 ♣    │
│       │
│   ♣   │
│       │
│    ♣ 4│
└───────┘
    ''',
    5: '''
┌───────┐
│5      │
│   ♠   │
│   ♠   │
│   ♠   │
│      5│
└───────┘
    ''',
    6: '''
┌───────┐
│6      │
│   ♦   │
│   ♦   │
│   ♦   │
│      6│
└───────┘
    ''',
    7: '''
┌───────┐
│7 ♣    │
│       │
│   ♣   │
│       │
│    ♣ 7│
└───────┘
    ''',
    8: '''
┌───────┐
│8      │
│   ♥   │
│   ♥   │
│   ♥   │
│      8│
└───────┘
    ''',
    9: '''
┌───────┐
│9      │
│   ♠   │
│   ♠   │
│   ♠   │
│      9│
└───────┘
    ''',
    10: '''
┌───────┐
│10 ♦   │
│   ♦   │
│   ♦   │
│   ♦ 10│
└───────┘
    ''',
    20: '''
┌───────┐
│J      │
│   ♣   │
│       │
│   ♣   │
│      J│
└───────┘
    ''',
    30: '''
┌───────┐
│Q      │
│   ♥   │
│   ♥   │
│   ♥   │
│      Q│
└───────┘
    ''',
    40: '''
┌───────┐
│K ♠    │
│       │
│   ♠   │
│       │
│    ♠ K│
└───────┘
    '''
}

def Deal_card():
    """Returns a random card from the deck."""
    deck_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards = random.choice(deck_of_cards)
    return cards

def clear():
    if os.name == 'posix':  # for Mac and Linux
        _ = os.system('clear')
    else:  # for Windows
        _ = os.system('cls')


def Calculate_score(played_cards):
    """Returns the sum of cards"""
    sum_card = 0
    for card in played_cards:
        sum_card += card
    if played_cards[0]+played_cards[1] == 21 and len(played_cards) == 2:
        return 21
    if sum_card > 21 and 11 in played_cards:
        index11 = played_cards.index(11)
        played_cards[index11] = 1
        
    return sum_card

def Winner(player,dealerr):
    """Returns the winner of the game"""
    if player == dealerr: return "Push!"
    elif dealerr == 0: return "Lose! Dealer has a BlackJack!"
    elif player > 21: return "You went over! you lose."
    elif player == 0: return "Congratulations....You got a BlackJack!"
    elif dealerr > 21: return "You won!"
    elif player > dealerr: return "You won!"
    else: return "You lose!"


def Black_Jack():
    """Main BlackJack Game"""
    user = []
    dealer = []
    for _ in range(2):
        user.append(Deal_card())
        dealer.append(Deal_card())

    replay = False

    while not replay:
        user_score = Calculate_score(user)
        dealer_score = Calculate_score(dealer)

        print("Your Cards are:")
        for i in user:
            if i == 10:
                keys = random.choice([10, 20, 30, 40])
                print(deck[keys])
            elif 1 in user:
                index1 = user.index(1)
                user[index1] = 11
            else:
                keys = i
                print(deck[keys])
        print(f"Current score: {user_score}!")

        if dealer[0] == 10:
            keyz = random.choice([10, 20, 30, 40])
        else:
            keyz = user[0]
        print(f"\nDealer card is: {deck[keyz]}")
            
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            print(f"You are {user_score - 21} points more than 21!\nGame over.")
            replay = True
        else:
            hit = input("Do you want to hit another card? 'Y' for Yes and 'N' for No\n").lower()
            if hit == "y":
                user.append(Deal_card())
                user_score = Calculate_score(user)
                print("\nYour new card is:")
                if user[0] == 10:
                    chosen_key = random.choice([10, 20, 30, 40])
                elif 1 in user:
                    chosen_key = 11
                    user_score = Calculate_score(user)
                else:
                    chosen_key = user[0]

                print(deck[chosen_key])
            else:
                replay = True

    while dealer_score != 0 and dealer_score < 17:
        dealer.append(Deal_card())
        dealer_score = Calculate_score(dealer)

        if 10 in dealer:
            chosen_keyz = random.choice([10, 20, 30, 40])
            index10 = dealer.index(10)
            dealer[index10] = chosen_keyz
        elif 1 in dealer:
            index1_u = dealer.index(1)
            dealer[index1_u] = 11
            dealer_score = Calculate_score(dealer)
        

        print("\nDealer's final hand:")
        for cardzz in dealer:
            print(deck[cardzz])

        print(dealer)
        print(f"Dealer's total Score: {dealer_score}\n")

        print(f"\nYour final hand:")
        for cadzz in user:
            print(deck[cadzz])

        print(user)
        print(f"Your total score: {user_score}")



    print(Winner(player=user_score,dealerr=dealer_score))


    if input("Restart game? 'R' for Restart: ").lower() == "r":
        clear()
        Black_Jack()

Black_Jack()
