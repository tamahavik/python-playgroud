from art import logo, vs
from data import data
import random

win_count = 0


def get_data():
    return random.choice(data)


def compare(a, b, c):
    if a > b and c == "a":
        return True
    elif b > a and c == "b":
        return True
    else:
        return False


def show_score():
    if win_count > 0:
        print(f"You are right current score {win_count}")


a = get_data()
b = get_data()
show_score()
print(logo)
print(f"Compare A : {a['name']}, {a['description']}, {a['country']}")
print(vs)
print(f"Against B : {b['name']}, {b['description']}, {b['country']}")
user_choice = input("Who has more followers? Type 'A' or 'B'? ").lower()
yes = compare(a=a["follower_count"], b=b["follower_count"], c=user_choice)
if yes:
    print("you win")
else:
    print("you lose")
