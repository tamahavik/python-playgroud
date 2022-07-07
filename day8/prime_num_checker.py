def prime_checker(number):
    is_prime = False
    for i in range(2, number):
        if number % i == 0:
            is_prime = True
            break

    if is_prime :
        print("PRIME")
    else:
        print("NOT PRIME")


n = int(input("check this number : "))
prime_checker(number=n)
