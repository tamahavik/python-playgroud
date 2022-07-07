year = int(input("Witch year you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP!")
        else:
            print("NOT LEAP!")
    else:
        print("LEAP!")
else:
    print("NOT LEAP!")
