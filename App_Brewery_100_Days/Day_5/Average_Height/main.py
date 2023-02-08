student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


number_of_students = 0
heights_sum = 0
for student in student_heights:
    heights_sum += student
    number_of_students += 1

median_height = int(round(heights_sum/number_of_students,0))
print(median_height)