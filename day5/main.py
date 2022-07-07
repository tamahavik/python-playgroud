fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# sum(list), max(list), min(list)

# range(start_include, end_exclude, step)
total = 0
for number in range(1, 101):  # 1 include 10 exclude
    total += number
print(total)
