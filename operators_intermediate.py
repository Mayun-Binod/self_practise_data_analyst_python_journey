# Take marks and check whether the student passed using >=.
marks = float(input("Enter your marks: "))
if marks >= 40:
    print("Passed")
else:
    print("Failed")

# Take two numbers and display which one is greater using if-else.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
if number1 > number2:
    print("First number is greater")
else:
    print("Second number is greater")

# Take a number and check whether it is even or odd using %.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Take a number and check whether it is divisible by both 3 and 5 using and.
number4 = int(input("Enter a number: "))
if number4 % 3 == 0 and number4 % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")

# Take a person's age and check whether they are between 18 and 60 using and.
age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("Age is between 18 and 60")
else:
    print("Age is not between 18 and 60")

# Take a username and check whether it exists in a list of usernames using in.
usernames = ["binod", "ram", "sita", "hari"]
username = input("Enter username: ")
if username in usernames:
    print("Username exists")
else:
    print("Username does not exist")

# Take a fruit name and check whether it is not available in a fruit list using not in.
fruits = ["apple", "banana", "mango", "orange"]
fruit = input("Enter fruit name: ")
if fruit not in fruits:
    print("Fruit is not available")
else:
    print("Fruit is available") 

# Create a shopping bill and use += to add three product prices and -= to apply a discount.
bill = 0
price1 = float(input("Enter price of product 1: "))
bill += price1
price2 = float(input("Enter price of product 2: "))
bill += price2
price3 = float(input("Enter price of product 3: "))
bill += price3
print("Total before discount:", bill)
discount = float(input("Enter discount amount: "))
bill -= discount
print("Final bill:", bill)