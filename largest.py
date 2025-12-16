"""
Program: Find the Largest of Three Numbers

This program accepts three numbers from the user
and displays the largest among them.
"""

# --------------------------------------------------
# INPUT
# --------------------------------------------------

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# --------------------------------------------------
# LOGIC TO FIND LARGEST
# --------------------------------------------------

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

print("The largest number is:", largest)

# --------------------------------------------------
# END OF PROGRAM
# --------------------------------------------------
