import pandas

student_dict = {
    "student": ["angela", "james", "lily"],
    "score": [56, 76, 98]
}

# looping through dictionary
# for (key, value) in student_dict.items():
    # print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through data frame
# for (key, value) in student_data_frame.items():
    # print(key)
    # print(value)

# in-build loop pandas
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row["student"])
    # print(row["score"])
    if row["student"] == "angela":
        print(row["score"])
