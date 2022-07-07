import os

bidders = {}


def get_winner():
    winner = ""
    high_bid = 0
    for key in bidders:
        if bidders[key] > high_bid:
            winner = key
            high_bid = bidders[key]
    print(f"The winner is {winner} with a bid of ${high_bid}")


print("Welcome to the secret auction program.")
other_bidder = True
while other_bidder:
    name = input("What is your name? ")
    bid = int(input("What your bid? $"))
    other = input("Other bidders? Type 'yes' or 'no'/ \n")
    bidders[name] = bid
    if other == "yes":
        other_bidder = True
        os.system("cls")
    else:
        other_bidder = False
        os.system("cls")
        get_winner()
