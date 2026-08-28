# Take two numbers and check whether the first number is greater or the second number is greater.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("First number is greater")
else:
    print("Second number is greater")

# Take marks and check whether the student passed or failed, where passing marks are 40.
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("You passed")
else:
    print("You failed")

# Take a number and check whether it is divisible by both 3 and 5 or not.  
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")

# Take age and check whether the person is between 18 and 60 or not.
age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("Age between 18 and 60")
else:
    print("Age not between 18 and 60")

# Take username and password and check whether both are correct or not
username = input("Enter username: ")
password = input("Enter password: ")
if username == "sandhya" and password == "12345":
    print("Username and password are correct")
else:
    print("Username or password is incorrect")

# Take marks and attendance and check whether the student is eligible or not eligible for an exam
marks = int(input("Enter your marks: "))
attendance = float(input("Enter your attendance: "))
if marks >= 40 and attendance >= 75:
    print("You are eligible for the exam")
else:
    print("You are not eligible for the exam")

# Take a number and check whether it is a two-digit number or not.
number = int(input("Enter a number: "))
if number >= 10 and number <= 99:
    print("It is a two-digit number")
else:
    print("It is not a two-digit number")

# Take a person's age and check whether they are eligible or not eligible for a driving license.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for a driving license")
else:
    print("You are not eligible for a driving license")


