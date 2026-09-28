# # Ask the user to enter a number.
# # Use try to convert the input into an integer.
# # Use except to handle invalid input.
# # Use else to display "Input is valid" when there is no error.
# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input. Please enter a number.")
# else:
#     print("Input is valid")

# Ask the user for two numbers and calculate their division.
# Use:
# try → perform the calculation
# except → handle the error
# else → display the result when successful
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except Exception as e:
    print("Error:", e)
else:
    print( result)