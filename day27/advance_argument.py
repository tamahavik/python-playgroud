# def function(a, b=2, c=3):
#     print(a, b, c)
#
#
# function(1)


# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     print(result)
#
#
# add(3, 4, 5, 6, 7, 8, 9, 10)


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    # print(f"this is : {kwargs['add']}")
    n += kwargs["add"]
    n *= kwargs["multipy"]
    print(n)


calculate(2, add=3, multipy=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seat = kwargs.get("seat")


car = Car(make="Nissan", model="GTR")
print(car.model)
print(car.make)
