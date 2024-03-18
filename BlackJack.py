import random
from replit import clear

blackjack = [''' 
 -------
|A      |
|       |
|       |
|       |
|      A|
 ------- ''','''
 -------
|2      |
|       |
|       |
|       |
|      2|
 ------- ''','''
 -------
|3      |
|       |
|       |
|       |
|      3|
 ------- ''','''
 -------
|4      |
|       |
|       |
|       |
|      4|
 ------- ''','''
 -------
|5      |
|       |
|       |
|       |
|      5|
 ------- ''','''
 -------
|6      |
|       |
|       |
|       |
|      6|
 ------- ''','''
 -------
|7      |
|       |
|       |
|       |
|      7|
 ------- ''', '''
 -------
|8      |
|       |
|       |
|       |
|      8|
 ------- ''','''
 -------
|9      |
|       |
|       |
|       |
|      9|
 ------- ''','''
 -------
|10     |
|       |
|       |
|       |
|     10|
 ------- ''',''' 
 -------
|J      |
|       |
|       |
|       |
|      J|
 ------- ''','''
 -------
|K      |
|       |
|       |
|       |
|      K|
 ------- ''', '''
 -------
|Q      |
|       |
|       |
|       |
|      Q|
 ------- ''']
def Deal_card():
    """Returns a random card from the deck."""
    deck_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards = random.choice(deck_of_cards)
    return cards

def Calculate_score(played_cards):
    """Returns the sum of cards"""
    sum = 0
    for card in played_cards:
        sum += card
    if played_cards[0]+played_cards[1] == 21 and len(played_cards) == 2: return 0
    if 11 in played_cards and sum > 21:
        played_cards.remove(11)
        played_cards.append(1)
        
    return sum

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
    while True:
        user_score = Calculate_score(played_cards=user)
        dealer_score = Calculate_score(played_cards=dealer)
        print(f"Your Cards are {blackjack[user[0]-1]} {blackjack[user[1]-1]}, your score is {user_score}")
        print(f"Dealer's cards are {blackjack[dealer[0]-1]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            break
        else:
            hit = input("Do you want to hit another card? ").lower()
            if hit == "y":
                user.append(Deal_card())
            else:
                break

    while dealer_score != 0 and dealer_score < 17:
            dealer.append(Deal_card())
            dealer_score = Calculate_score(played_cards=dealer)
    print(f"Your Final Hand :{blackjack[user[0]-1]} {blackjack[user[1]-1]} {blackjack[user[2]-1]}, Final score is {user_score}")
    print(f"Dealer's Final Hand :{blackjack[dealer[0]-1]} {blackjack[dealer[1]-1]}, Final score is {dealer_score}")
    print(Winner(player=user_score,dealerr=dealer_score))

Black_Jack()

if input("Restart game: ") == "r":
    clear()
    Black_Jack()





        





