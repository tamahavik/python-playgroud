# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# print(new_list)

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "tama"
new_list = [letter for letter in name]
print(new_list)

new_list = [n * 2 for n in range(1, 5)]
print(new_list)

names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
short_name = [name for name in names if len(name) < 5]
print(short_name)
long_upper = [name.upper() for name in names if len(name) > 5]
print(long_upper)
