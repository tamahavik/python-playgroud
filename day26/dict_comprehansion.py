import random

names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
student_score = {student: random.randint(1, 101) for student in names}
print(student_score)

passed_student = {key: value for (key, value) in student_score.items() if value >= 60}
print(passed_student)
