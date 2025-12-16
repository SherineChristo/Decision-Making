"""
Program: Student Report Card

This program accepts student details and marks for subjects,
calculates total, average, grade, and displays a formatted report.
"""

# --------------------------------------------------
# INPUT
# --------------------------------------------------

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Marks for 5 subjects
subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]
marks = []

for subject in subjects:
    score = float(input(f"Enter marks for {subject} (out of 100): "))
    marks.append(score)

# --------------------------------------------------
# CALCULATION
# --------------------------------------------------

total_marks = sum(marks)
average_marks = total_marks / len(subjects)

# Grade assignment
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 50:
    grade = "D"
else:
    grade = "Fail"

# --------------------------------------------------
# OUTPUT: Report Card
# --------------------------------------------------

print("\n------ Student Report Card ------")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Subjects & Marks:")

for i in range(len(subjects)):
    print(f"{subjects[i]} : {marks[i]}")

print("Total Marks:", total_marks)
print("Average    :", average_marks)
print("Grade      :", grade)
print("--------------------------------")

# --------------------------------------------------
# END OF PROGRAM
# --------------------------------------------------
