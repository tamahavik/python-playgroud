print("Welcome to the love calculator!")
name1 = input("Input your name? ")
name2 = input("Input their name? ")

t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u")
e1 = name1.lower().count("e") + name2.lower().count("e")
l = name1.lower().count("l") + name2.lower().count("l")
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")
e2 = name1.lower().count("e") + name2.lower().count("e")

score1 = t + r + u + e1
score2 = l + o + v + e2
love_score_str = str(score1) + str(score2)
love_score = int(love_score_str)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together live coke and mentos")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
