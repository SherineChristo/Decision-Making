"""
Program: Check Leap Year

This program checks whether a given year
is a leap year or not.
"""

# --------------------------------------------------
# INPUT
# --------------------------------------------------

year = int(input("Enter a year: "))

# --------------------------------------------------
# LEAP YEAR LOGIC
# --------------------------------------------------

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# --------------------------------------------------
# END OF PROGRAM
# --------------------------------------------------
