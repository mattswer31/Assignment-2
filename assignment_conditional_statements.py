# 1. Decisions at the Crossroad
# Task 1 - Code Correction
number = int(input("enter a number: ")) #need to cast input from str to int
if number > 0:
    print("The number is positive")
elif number == 0: #== not =
    print("number is zero")
else: #cannot add condition to else, and is also unnecssary 
    print("number is negative")

# 2. The Greatest Showdown
# Task 1 and 2 - Identify the Greatest and Smallest
x = int(input("First number?"))
y = int(input("Second number?"))
z = int(input("Third number?"))
greatest = 0
smallest = 0
if x >= y and x >= z:
    greatest = x
elif y >= x and y >= z:
    greatest = y
else:
    greatest = z
print(str(greatest) + " is the greatest number")
if x <= y and x <= z:
    smallest = x
elif y <= x and y <= z:
    smallest = y
else:
    smallest = z
print(str(smallest) + " is the smallest number")

# 3. Leap Year Explorer
# Task 1: Leap Year Checker
year = int(input("Input a year"))
if year % 4 == 0 and year % 100 !=0:
    print(str(year) + " is a leap year.")
elif year % 400 == 0:
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")

