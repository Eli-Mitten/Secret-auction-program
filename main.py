import os
from art import logo

print(logo)

bidding_finish = False
bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bit of ${highest_bid}")

while not bidding_finish:
    auction = {}
    name = input("Write your name: ")
    amount = int(input("What is you auction? $"))
    auction["name"] = name
    auction["amount"] = amount
    bids[name] = amount
    should_continue = input("another bidder? Y or N: ")
    if should_continue.upper() != "Y":
        bidding_finish = True
    else:
        os.system('cls||clear')
        
find_highest_bidder(bids)