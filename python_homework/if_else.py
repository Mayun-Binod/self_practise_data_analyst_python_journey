# Take a number and check whether it is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#    Take a number and check whether it is even or odd. 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Take a person's age and check whether they are eligible to vote.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Take marks and display:
# 80–100 → A
# 60–79 → B
# 40–59 → C
# Below 40 → Fail
marks = int(input("Enter your marks: "))
if marks >= 80 and marks <= 100:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
elif marks >= 0:
    print("Fail")
else:
    print("Invalid marks")

# Take three numbers and find the largest number.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is the largest")

elif b > a and b > c:
    print(b, "is the largest")

elif c > a and c > b:
    print(c, "is the largest")

else:
    print("numbers are equal")

# Create a simple login system using username and password. solve this
username = input("Enter username: ")
password = input("Enter password: ")
if username == "sandhya" and password == "12345":
    print("Login successful")
else:
    print("incorrect username or password")