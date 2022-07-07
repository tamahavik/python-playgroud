student_heights = input("input list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

count = 0
total = 0
for height in student_heights:
    total += height
    count += 1

average = round(total / count)
print(average)
