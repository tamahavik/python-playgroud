# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file_name:
    names = file_name.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

for name in names:
    with open(f"./Output/ReadyToSend/{name.strip()}", mode="w") as done:
        write_letter = letter.replace(PLACEHOLDER, name.strip())
        done.write(write_letter)
