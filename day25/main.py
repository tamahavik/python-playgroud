import pandas

# data = pandas.read_csv("./weather_data.csv")
#
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
#
# average_temp = sum(temp_list) / len(temp_list)
# print(round(average_temp, 3))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Working with column
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "student": ["any", "James", "Angela"],
#     "score": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("./new_data_csv")

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("./count_fur_data.csv")
