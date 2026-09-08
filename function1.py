# Create a function that takes two numbers and returns their sum.
def addition(a, b):
    return a + b

result = addition(10, 20)
print(result)

# Create a function that takes a number and returns its square.
def square(number):
    return number ** 2

result = square(5)
print(result)

# Create a function that takes a number and returns its cube.
def cube(number):
    return number ** 3

result = cube(5)
print(result)

# Create a function that takes a number and returns whether it is even or odd.
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_odd(7)
print(result)

# Create a function that takes length and width and returns the area of a rectangle.
def rectangle_area(length, width):
    return length * width

result = rectangle_area(10, 5)
print(result)

# Create a function that takes the radius of a circle and returns its area.
def circle_area(radius):
    return 3.14159 * radius ** 2

result = circle_area(5)
print(result)

# Create a function that takes principal, rate, and time and returns simple interest.
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

result = simple_interest(10000, 5, 2)
print(result)





