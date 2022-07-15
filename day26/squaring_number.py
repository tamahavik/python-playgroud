numbers = [1, 1, 2, 3, 5, 8, 13, 21, 24, 55]
squared_number = [num ** 2 for num in numbers]
print(squared_number)

even_number = [num for num in numbers if num % 2 == 0]
print(even_number)
 