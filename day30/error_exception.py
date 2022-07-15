# FileNotFound

# try:
#     file = open("/.file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("./file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"the key {error_message} not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error i made")

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_exist_key"]

# IndexError
# fruit_list = ["apple"]
# fruit = fruit_list[2]

# TypeError
# text = "acb"
# print(text + 5)

height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("human height should not over 3 meters")

bmi = weight / height ** 2

print(bmi)
