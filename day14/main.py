import os

from art import logo, vs
from data import data
import random


def get_data():
    return random.choice(data)


def format_data(account):
    return f"{account['name']}, {account['description']}, {account['country']}"


def compare(a, b, c):
    if a > b and c == "a":
        return True
    elif b > a and c == "b":
        return True
    else:
        return False


# def show_score():
#     print(f"You are right current score {win_count}")
#     print(f"Sorry, that's wrong, final score {win_count}")
print(logo)
win_count = 0
game_should_continue = True
b = get_data()

while game_should_continue:
    a = b
    b = get_data()
    while a == b:
        b = get_data()

    print(f"Compare A : {format_data(a)}")
    print(vs)
    print(f"Against B : {format_data(b)}")
    user_choice = input("Who has more followers? Type 'A' or 'B'? ").lower()
    yes = compare(a=a["follower_count"], b=b["follower_count"], c=user_choice)
    os.system("cls")
    print(logo)
    if yes:
        win_count += 1
        print(f"you win, current score {win_count}")
    else:
        print(f"you lose, final score {win_count}")
        game_should_continue = False

