# Ask the user to enter two numbers and perform division. Use Exception as e to display the actual error message.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(result)

except Exception as e:
    print("Something went wrong", e)

# Write a program that performs a mathematical calculation inside try. If an error occurs, display the error using e.
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = (num1 + num2) / num2
    print( result)
except Exception as e:
    print("Error:", e)

# Create a program that intentionally causes an error and use Exception as e to show what type of problem occurred.
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except Exception as e:
    print("Something went wrong", e)