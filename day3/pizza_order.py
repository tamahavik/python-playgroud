print("Welcome to python pizza deliveries!")
size = input("What size pizza you want? S, M, or L? ")
add_papperoni = input("Do you want papperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

final_bill = 0
if size == "S":
    final_bill = 15
    if add_papperoni == "Y":
        final_bill += 2
elif size == "M":
    final_bill = 20
    if add_papperoni == "Y":
        final_bill += 3
else:
    final_bill = 25
    if add_papperoni == "Y":
        final_bill += 3

if extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is ${final_bill}")
