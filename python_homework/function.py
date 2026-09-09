# Create a function that prints "Hello Python".
def hello():
    print("Hello Python")
hello()

# Create a function that takes a name as a parameter and prints a greeting.
def greet(name):
    print(f"Hello, {name}")
greet("sandhya")

# Create a function that takes two numbers and prints their sum.
def two_numbers(a, b):
    print(a + b)
two_numbers(10, 20)

# Create a function that takes two numbers and returns their sum.
def return_numbers(a, b):
    return a + b
result = return_numbers(10, 20)
print(result)

# Create a function that takes a number and returns whether it is even or odd.
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = even_odd(10)
print(result)

# Create a function that takes a number and returns whether it is positive, negative, or zero.
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
result = check_number(5)
print(result)

# Create a function that takes length and width and returns the area of a rectangle.
def rectangle_area(length, width):
    return length * width
result = rectangle_area(10, 5)
print(result)

# Create a function that takes the radius of a circle and returns its area.
def circle_area(PI):
    return 3.1415 * PI * PI
result = circle_area(5)
print(result)

# Create a function that takes principal, rate, and time and returns simple interest.
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
result = simple_interest(10000, 5, 2)
print(result)

# Create a function that takes three numbers and returns the largest number
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
result = largest(10, 25, 15)
print(result)

# Create a function that takes a number and returns its factorial. solve this
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


answer = factorial(5)
print(answer)

# Create a student result program using a function.

# The program should:

# Take student's name
# Take marks in 3 subjects
# Calculate total
# Calculate percentage
# Determine grade using if/elif/else
# Return the final result
# Print the result neatly SOLVE THIS
def student_result(name, math, science, english):
    total = math + science + english
    percentage = total / 3

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return name, total, percentage, grade

name = input("Enter student's name: ")
math = float(input("Enter marks in Math: "))
science = float(input("Enter marks in Science: "))
english = float(input("Enter marks in English: "))

result = student_result(name, math, science, english)

print("\n----- Student Result -----")
print("Name:", result[0])
print("Total:", result[1])
print("Percentage:", result[2], "%")
print("Grade:", result[3])






