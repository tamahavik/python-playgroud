def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What the first number? "))
    for symbol in operations:
        print(symbol)
    flag = True
    while flag:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What the next number? "))
        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cons = input(f"Type 'y' for continue calculating with {answer}, or type 'n' to new calculation")
        if cons == "y":
            num1 = answer
        else:
            flag = False
            calculator()


calculator()
