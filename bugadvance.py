
# ==========================================
# Python Bugs and Errors
# Beginner to Intermediate Practice
# ==========================================


# 1. LOGICAL BUG
# The program runs but produces the wrong result.

num1 = 10
num2 = 5

result = num1 - num2  # Bug: should use + for addition
print("Bug example:", result)


# 2. SYNTAX ERROR
# Happens when Python syntax is incorrect.
# Uncomment the next line to test:
# if 10 > 5 print("Yes")


# 3. INDENTATION ERROR
# Happens when code indentation is incorrect.
# Uncomment the next lines to test:
# if True:
# print("Hello")


# 4. NAME ERROR
# Happens when a name has not been defined.
# Uncomment to test:
# print(student_name)


# 5. TYPE ERROR
# Happens when incompatible data types are used.
# Uncomment to test:
# print(10 + "20")


# 6. VALUE ERROR
# Happens when a value cannot be converted as requested.
# Uncomment to test:
# age = int("hello")


# 7. INDEX ERROR
# Happens when a list index does not exist.
# Uncomment to test:
# numbers = [10, 20, 30]
# print(numbers[5])


# 8. KEY ERROR
# Happens when a dictionary key does not exist.
# Uncomment to test:
# student = {"name": "Binod"}
# print(student["age"])


# 9. ZERO DIVISION ERROR
# Happens when a number is divided by zero.
# Uncomment to test:
# print(10 / 0)


# 10. ATTRIBUTE ERROR
# Happens when an object does not have the requested method.
# Uncomment to test:
# name = "Binod"
# name.append("Kumar")


# 11. FILE NOT FOUND ERROR
# Happens when the requested file cannot be found.
# Uncomment to test:
# with open("missing_file.txt", "r") as file:
#     print(file.read())


# 12. MODULE NOT FOUND ERROR
# Happens when Python cannot find a module.
# Uncomment to test:
# import unknown_module_xyz


# 13. OVERFLOW ERROR
# Happens when a numeric operation exceeds a function's limit.
# Example:
# import math
# print(math.exp(10000))


# 14. IMPORT ERROR
# Happens when an import cannot find the requested name.
# Uncomment to test:
# from math import unknown_function


# 15. TRY AND EXCEPT
# Handle an error without stopping the whole program.

try:
    number = int(input("Enter a whole number: "))
    print("Your number is:", number)

except ValueError:
    print("Invalid input. Please enter a whole number.")


# 16. EXCEPTION AS E
# Displays the error message.

try:
    result = 10 / 0

except Exception as e:
    print("Error message:", e)


# 17. ELSE
# Runs when no exception occurs inside try.

try:
    number = int(input("Enter a number to check: "))

except ValueError:
    print("Please enter a valid whole number.")

else:
    print("You entered:", number)


# 18. FINALLY
# Runs whether an exception occurs or not.

try:
    print("Program is running.")

except Exception as e:
    print("An error occurred:", e)

finally:
    print("This block always runs.")


# 19. RAISE
# Used to raise an error intentionally.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age is valid.")


try:
    check_age(-5)

except ValueError as e:
    print("Age error:", e)


# 20. CUSTOM EXCEPTION
# Create your own exception type.

class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance.")

    return balance - amount


try:
    remaining_balance = withdraw(1000, 1500)
    print("Remaining balance:", remaining_balance)

except InsufficientBalanceError as e:
    print("Withdrawal error:", e)


print("\nPython error practice completed.")