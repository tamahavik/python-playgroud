import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(now)
# print(year)
# print(month)
# print(day_of_week)

date_of_birth = dt.datetime(year=2020, month=1, day=1)
print(date_of_birth)
