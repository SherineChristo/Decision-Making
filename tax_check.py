"""
Program: Tax Check Based on Salary

This program accepts a name and salary from the user,
checks if the salary is greater than 3,00,000 (3L),
and displays if they must pay tax.
"""



name = input("Enter your name: ")
salary = float(input("Enter your salary (in INR): "))



if salary > 300000:
    print(name, "must pay tax.")
else:
    print(name, "does not need to pay tax.")


