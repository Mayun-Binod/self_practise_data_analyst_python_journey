# Create a function welcome() that prints "Welcome to Python".
def welcome():
    print("Welcome to Python")
welcome()

# Create a function that accepts a name and prints a greeting.
def greeting(name):
    print("Hello", name)
greeting("sandhya")

# Create a function that accepts name and age and prints both.
def person(name, age):
    print("Name:", name)
    print("Age:", age)
person("prakriti", 25)

# Create a function that accepts two numbers and prints their sum.
def add(a, b):
    print(a + b)
add(10, 20)

# Create a function that accepts two numbers and returns their sum.
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print(result)

# Create a function that accepts two numbers and returns:
# addition
# subtraction
# multiplication
# division
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division
result = calculate(20, 5)
print(result)

# Create a function that accepts a number and returns its square.
def square(number):
    return number * number
print(square(5))

# Create a function that accepts length and width and returns the area of a rectangle.
def rectangle_area(length, width):
    return length * width
print(rectangle_area(10, 5))

# Create a function that accepts a number and returns whether it is positive, negative, or zero.
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(7))




