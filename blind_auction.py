"""
    Introduction:
        --> Build a program that takes name and bidding price for a secret bidding 
            and ask if there is any more bidder in room if yes then make screen clear 
            and let another bidder do the same. And no bidder is left then show the
            winners name and its bid.
"""
import os
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Alok": 123, "Angela": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("Bider name: ").capitalize()
    price = int(input("Biding amount: ₹"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type y/n ").lower()
    if should_continue == "n":
        bidding_finished = True
        find_highest_bidder(bidding_record= bids,)
    elif should_continue == 'y':
        os.system('cls')        
