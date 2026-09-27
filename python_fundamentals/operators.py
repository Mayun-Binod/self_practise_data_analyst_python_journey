# Take your name, age, and city as input and print them.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
print(f"Name: {name}, Age: {age}, City: {city}")

# Take two numbers and print their sum, difference, multiplication, and division.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")

# Take the length and width of a rectangle and calculate its area.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(area)

# Take a number and calculate its square and cube.
number = int(input("Enter a number: "))
print("Square:", number ** 2)
print("Cube:", number ** 3)

# Take marks of 5 subjects and calculate total and average.
mark1 = float(input("Enter marks subject 1:"))
mark2 = float(input("Enter marks subject 2:"))
mark3 = float(input("Enter marks  subject 3:"))
mark4 = float(input("Enter marks  subject 4:"))
mark5 = float(input("Enter marks  subject 5:"))
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5
print(total)
print(average)