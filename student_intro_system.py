# Student Introduction System
# This program collects and displays details of multiple students
# Concepts used: Loops, User Input, Variables, Data Types

n = int(input("Enter number of students in class: "))

for i in range(n):

    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    branch = input("Enter branch: ")
    student_id = input("Enter ID: ")
    grade = float(input("Enter grade: "))

    print("\n----- Student Details -----")

    print("Name   :", name)
    print("Age    :", age)
    print("Branch :", branch)
    print("ID     :", student_id)
    print("Grade  :", grade)

    print("---------------------------")
