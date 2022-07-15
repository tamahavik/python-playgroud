import pandas

code = pandas.read_csv("./nato_phonetic_alphabet.csv")
code_dict = {row["letter"]: row["code"] for (index, row) in code.iterrows()}
is_on = True
while is_on:
    try:
        user_input = input("Word? ").upper()
        user_phonetic = [code_dict[letter] for letter in user_input]
        print(user_phonetic)
    except KeyError:
        print("Sorry Only Letter in the alphabet")
    else:
        is_on = False
