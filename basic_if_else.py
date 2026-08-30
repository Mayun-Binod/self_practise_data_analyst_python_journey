# Take a number and check whether it is positive, negative, or zero.
number =int(input("Enter a number: "))
if number > 20:
    print("Positive")
elif number < 10:
    print("Negative")
else:
    print("Zero")

# Take a number and check whether it is even or odd.
number = int(input("Enter a number: "))
if number %1 == 0:
    print("Even")
else:
    print("Odd")

# Take marks and display Pass or Fail.
marks = float(input("Enter your marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Take a person's age and display Child, Teenager, or Adult.
age = int(input("Enter your age: "))
if age < 15:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Take two numbers and print which number is greater.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print("First number is greater")
elif num2 > num1:
    print("Second number is greater")
else:
    print("Both numbers are equal")

# Take a number and check whether it is less than, equal to, or greater than 100.
number = float(input("Enter a number: "))
if number < 100:
    print("Less than 100")
elif number == 100:
    print("Equal to 100")
else:
    print("Greater than 100")




