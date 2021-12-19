student_heights = input("Input a list of student heights ").split()
i = 0
total = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

for student_height in student_heights:
    total += student_height
    i += 1

print(student_height)
print(f"Average = {round(total/i)}")

##################
# total = sum(student_heights)
# number_of_student = len(student_heights)
# average = round(total/number_of_student)
