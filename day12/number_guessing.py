import random

answer = random.randint(1, 101)

difficulty = {
    "easy": 10,
    "hard": 5
}


def checking(guess):
    global answer
    print(answer)
    if guess > answer:
        print("Too High")
        return False
    elif guess < answer:
        print("Too Low")
        return False
    else:
        print(f"You Got it! The answer was {answer}")
        return True


print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100")
difficulty_choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = difficulty[difficulty_choose]
end = True
while end:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    check = checking(guess)
    if not check:
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            end = False
        else:
            end = True
    else:
        attempts = 0
        end = False
