# type() for get type data
print(type(2 / 3))

# len(string) for get length
print(len("hello world!"))

# round(float, digit) for remove floating number into int but round up not like int round down
print(8 / 3)
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))

# flow division ( // )
# in python division always return float, with flow division ( // )
# it will return int
print(type(8 / 3))
print(type(8 // 3))

# f-string in python
# insert all data type into string with f-string
score = 0
height = 1.8
isWinning = True
print(f"your score is {score} with {height} and is winning {isWinning}")
