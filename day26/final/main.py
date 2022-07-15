import pandas

code = pandas.read_csv("./nato_phonetic_alphabet.csv")
code_dict = {row["letter"]: row["code"] for (index, row) in code.iterrows()}
user_input = input("Word? ").upper()
# user_phonetic = [value for (key, value) in code_dict.items() if key in user_input]
user_phonetic = [code_dict[letter] for letter in user_input]
print(user_phonetic)
