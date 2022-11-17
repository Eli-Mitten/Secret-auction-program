import os
from art import logo

print(logo)

other_auction = True
auctions = []
while other_auction:
    auction = {}
    name = input("Write your name: ")
    amount = int(input("What is you auction? $"))
    auction["name"] = name
    auction["amount"] = amount
    print(auction)
    auctions.append(auction)
    
    print(auctions)
    
    answer = input("another bidder? Y or N: ")
    if answer.upper() != "Y":
        other_auction = False
        
count = 0
best = 0
entry_number = 0
for i in auctions:
    count += 1
    if i["amount"] > best:
        best = i["amount"]
        entry_number = count

winner = auctions[entry_number - 1]
print(f'WINNER {winner["name"]} with {winner["amount"]}$')