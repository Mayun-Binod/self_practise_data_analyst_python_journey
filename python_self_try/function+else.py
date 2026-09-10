# Create a function that accepts age and returns:
# "Child"
# "Teenager"
# "Adult"
def age_category(age):
    if age < 15:
        return "Child"
    elif age < 20:
        return "Teenager"
    else:
        return "Adult"
print(age_category(19))

# Create a function that accepts marks and returns the grade.
def grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"
print(grade(75))

# Create a function that accepts three numbers and returns the largest.
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
    else:
        return c
print(largest(10, 25, 15))

# Create a function that accepts three numbers and returns the smallest.
def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c >= a and c >= b:
            return c
    else:
        return c
print(smallest(10, 25, 5))

# Create a function that checks whether a number is divisible by both 3 and 5.
def divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Divisible by both"
    else:
        return "Not divisible by both"
print(divisible_by_3_and_5(30))

# Create a function for a simple calculator using if/elif
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"
print(calculator(20, 5, "*"))

# Create a function that accepts username and password and returns "Login successful" or "Invalid login".
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid login"
print(login("admin", "1234"))



