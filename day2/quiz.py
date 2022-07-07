age = input("What is your current age? ")
int_age = int(age)
limit_life = 90
day = (limit_life - int_age) * 365
week = (limit_life - int_age) * 52
month = (limit_life - int_age) * 12

print(f"You have {day} days, {week} weeks, and {month} months left.")
