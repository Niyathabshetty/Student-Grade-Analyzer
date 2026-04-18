students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input("Enter marks: "))
    students.append((name, marks))

print("\n--- Grade Report ---")

for name, marks in students:
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(name + " - Marks: " + str(marks) + ", Grade: " + grade)

total = 0
for name, marks in students:
    total += marks

avg = total / n

print(f"\nAverage Marks: {avg}")