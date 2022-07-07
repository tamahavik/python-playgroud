student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_score:
    score = student_score[key]
    if score > 90:
        student_grades[key] = "A"
    elif score > 80:
        student_grades[key] = "B"
    elif score > 70:
        student_grades[key] = "C"
    else:
        student_grades[key] = "D"

print(student_grades)

