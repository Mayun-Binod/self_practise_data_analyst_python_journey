# Create a program that asks the user for two numbers and performs division.
# Your program must use:
# try
# except
# Exception as e
# else
# finally
# Handle invalid input and division by zero.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError as e:
    print("Invalid input:", e)
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
except Exception as e:
    print("Something went wrong:", e)
else:
    print("Result:", result)
finally:
    print("Program completed.")

# Create a program containing a list of five fruits. Ask the user to enter an index and display the fruit.
# Handle:
# Invalid input
# Invalid index
# Use try, except, and finally.
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
try:
    index = int(input("Enter an names: "))
    print("Fruit:", fruits[index])
except ValueError as e:
    print("Invalid input:", e)
except IndexError as e:
    print("Invalid index:", e)
finally:
    print("Program completed.")

# Create a simple calculator that asks the user for:
# First number:
# Second number:
# Operator:
# Support:
# +
# -
# *
# /
# Handle invalid numbers, division by zero, and invalid operators.
try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operator = input("Operator (+, -, *, /): ")
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("Invalid operator")
except ValueError as e:
    print("Invalid input:", e)
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
except Exception as e:
    print("Something went wrong:", e)
else:
    print("Result:", result)
finally:
    print("Calculator completed.")

# Create a student marks program that asks the user to enter marks for five subjects and calculates the total and average.
# Handle invalid input using exception handling.
try:
    marks1 = float(input("Enter marks English: "))
    marks2 = float(input("Enter marks Mathematics: "))
    marks3 = float(input("Enter marks Science: "))
    marks4 = float(input("Enter marks Computer: "))
    marks5 = float(input("Enter marks Nepali: "))
    total = marks1 + marks2 + marks3 + marks4 + marks5
    average = total / 5
except ValueError as e:
    print("Invalid marks", e)
except Exception as e:
    print("Something went wrong", e)
else:
    print("Total:", total)
    print("Average:", average)
finally:
    print("Marks calculation complete")

# Create a login program using a dictionary containing usernames and passwords.
# Ask the user for a username and password. Handle the situation when the username does not exist.
users = {
    "sandhya": "1234",
    "admin": "admin123",
    "student": "pass123"
}
try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username not in users:
        raise KeyError("Username does not exist")
    if users[username] == password:
        print("Login successful.")
    else:
        print("Incorrect password.")
except KeyError as e:
    print("Login error:", e)
except Exception as e:
    print("Something went wrong:", e)
finally:
    print("Login process completed.")
