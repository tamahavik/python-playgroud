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
print(data[data["Primary Fur Color"]])
