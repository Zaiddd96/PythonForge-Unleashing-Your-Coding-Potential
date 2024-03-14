from replit import clear
from artt import *
bids = {}
def highest_bid(bidding):
    high_bid = 0
    winner = ""
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"{winner} has won the auction with a bid of ${high_bid}")

print(auction)   
print("Welcome to the secret auction!")
while True:
    try:
        name = input("Enter your name: ")
        money = int(input("Enter the bid: $"))
    except ValueError:
        print("Invalid input. Please enter a valid bid amount as an integer.")
        continue
    bids[name] = money
    another = input("Are there any other bidders? 'yes' or 'no': ").lower()
    if another != "yes":
        highest_bid(bidding=bids)
        break
    else:
        clear()