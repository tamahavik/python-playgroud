print("WELCOME TO TREASURE ISLAND, Your mission is to find the treasure")
choice1 = input("Left or Right ? ").lower()
if choice1 == "left":
    choice2 = input("Swim or wait? ").lower()
    if choice2 == "wait":
        choice3 = input("Red, blue, or yellow? ").lower()
        if choice3 == "red":
            print("Burn by fire")
        elif choice3 == "blue":
            print("Eaten by beast")
        elif choice3 == "yellow":
            print("You win")
        else:
            print("Game Over")
    else:
        print("Game over")
else:
    print("Game over")
