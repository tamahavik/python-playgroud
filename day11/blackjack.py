from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(list_cards):
    score = sum(list_cards)
    if len(list_cards) == 2 and score == 21:
        return 0
    if 11 in list_cards and score > 21:
        list_cards.remove(11)
        list_cards.append(1)
        score = sum(list_cards)
    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        the_result = "Its Draw"
    elif user_score == 0:
        the_result = "You Win"
    elif computer_score == 0:
        the_result = "Computer Win"
    elif user_score > 21 and computer_score < 21:
        the_result = "Computer Win"
    elif user_score < 21 and computer_score > 21:
        the_result = "You Win"
    else:
        if user_score > computer_score:
            the_result = "You Win"
        else:
            the_result = "Computer Win"
    return the_result


flag_repeated = True
while flag_repeated:
    flag_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if flag_play == "y":
        your_card = []
        computer_card = []
        your_card.append(deal_card())
        your_card.append(deal_card())
        computer_card.append(deal_card())

        draw_card = "y"
        while draw_card == "y":
            print(f"Your cards: {your_card}, current score: {calculate_score(your_card)}")
            print(f"Computer first card: {computer_card[0]}")

            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == "y":
                your_card.append(deal_card())

        while calculate_score(computer_card) < 17:
            computer_card.append(deal_card())

        your_score = calculate_score(your_card)
        computer_score = calculate_score(computer_card)
        print(f"Your final hand {your_card}, final score: {calculate_score(your_card)}")
        print(f"Computer final hand {computer_card}, final score: {calculate_score(computer_card)}")
        result = compare(your_score, computer_score)
        print(result)
    else:
        flag_play = False
