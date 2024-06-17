grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)

students_dict = {}

for s in range(len(grades)):
    students_dict[students[s]] = sum(grades[s]) / len(grades[s])

print(students_dict)


