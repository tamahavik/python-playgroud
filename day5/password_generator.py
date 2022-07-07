import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome tho the PyPassword Generator")
total_letter = int(input("How many letters would you like in your password?\n"))
total_symbol = int(input("How many symbols would you like?\n"))
total_number = int(input("How many numbers would you like?\n"))

# first
total_word = total_letter + total_symbol + total_number
ch_list = ["l", "s", "n"]
password = ""
for n in range(0, total_word):
    x = random.randint(0, len(ch_list) - 1)
    if ch_list[x] == "l":
        password += random.choice(letters)
        total_letter -= 1
        if total_letter == 0:
            ch_list.remove("l")
    elif ch_list[x] == "s":
        password += random.choice(symbols)
        total_symbol -= 1
        if total_symbol == 0:
            ch_list.remove("s")
    else:
        password += random.choice(numbers)
        total_number -= 1
        if total_number == 0:
            ch_list.remove("n")

# you can use random.shuffle(list) for randomize inside list
print(password)
