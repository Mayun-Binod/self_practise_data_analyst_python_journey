# ==========================================
# Bugs and Errors in Python
# One File Example
# ==========================================


# ==========================================
# 1. BUG
# ==========================================

# A bug is a mistake in the program logic.
# The program may run, but the result is wrong.

num1 = 10
num2 = 5

# Bug: We wanted addition but used subtraction
result = num1 - num2

print("Bug Example:")
print("Expected:", 15)
print("Actual:", result)


# ==========================================
# 2. SYNTAX ERROR
# ==========================================

# SyntaxError happens when Python grammar is incorrect.

# Example:
# if 10 > 5
#     print("Yes")

# The colon (:) is missing.


# ==========================================
# 3. NAME ERROR
# ==========================================

# NameError happens when we use a variable
# that has not been created.

# Example:
# print(age)


# ==========================================
# 4. TYPE ERROR
# ==========================================

# TypeError happens when we use incompatible
# data types together.

# Example:
# age = 25
# print(age + " years")


# ==========================================
# 5. VALUE ERROR
# ==========================================

# ValueError happens when the data type is correct
# but the value is not valid.

# Example:
# age = int("hello")


# ==========================================
# 6. INDEX ERROR
# ==========================================

# IndexError happens when we try to access
# an index that does not exist.

# Example:
# numbers = [10, 20, 30]
# print(numbers[5])


# ==========================================
# 7. KEY ERROR
# ==========================================

# KeyError happens when we try to access
# a dictionary key that does not exist.

# Example:
# student = {"name": "Binod"}
# print(student["age"])


# ==========================================
# 8. ZERO DIVISION ERROR
# ==========================================

# ZeroDivisionError happens when we divide
# a number by zero.

# Example:
# number = 10
# result = number / 0


# ==========================================
# 9. ATTRIBUTE ERROR
# ==========================================

# AttributeError happens when an object does not
# have the method or attribute we try to use.

# Example:
# name = "Binod"
# name.append("Kumar")


# ==========================================
# 10. FILE NOT FOUND ERROR
# ==========================================

# FileNotFoundError happens when Python tries
# to open a file that does not exist.

# Example:
# file = open("student.txt", "r")


# ==========================================
# 11. MODULE NOT FOUND ERROR
# ==========================================

# ModuleNotFoundError happens when Python
# cannot find the requested module.

# Example:
# import abcxyz


# ==========================================
# SUMMARY
# ==========================================

print("\n========== Bugs and Errors ==========")

print("Bug              -> Mistake in program logic")
print("SyntaxError      -> Incorrect Python syntax")
print("NameError        -> Name or variable not found")
print("TypeError        -> Incompatible data types")
print("ValueError       -> Invalid value")
print("IndexError       -> Index does not exist")
print("KeyError         -> Dictionary key does not exist")
print("ZeroDivisionError -> Division by zero")
print("AttributeError   -> Attribute or method not found")
print("FileNotFoundError -> File does not exist")
print("ModuleNotFoundError -> Module cannot be found")