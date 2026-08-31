# Take two numbers and calculate their sum, difference, product, and division.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
print("Sum:", number1 + number2)
print("Difference:", number1 - number2)
print("Product:", number1 * number2)
print("Division:", number1 / number2)

# Take a number and find its square and cube.
number3 = float(input("Enter a number: "))
print("Square:", number3 ** 2)
print("Cube:", number3 ** 3)

# Take two numbers and find the remainder and floor division.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print("Remainder:", number1 % number2)
print("Floor Division:", number1 // number2)

# Take a number and check whether it is greater than 50.
number = int(input("Enter a number: "))
print(number >50)

# Take two numbers and check whether they are equal or not equal.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print("Equal:", number1 == number2)
print("Not Equal:", number1 != number2)

# Take a number and check whether it is between 10 and 100.
number = int(input("Enter a number: "))
if number >= 10 and number <= 100:
    print("Number is between 10 and 100")

# Take a person's age and check whether they are 18 or older using a comparison operator.
age = int(input("Enter your age: "))
if age >= 18:
    print("18 or older")
else:
    print("Under 18")

# Create a variable x = 10, then use assignment operators to add 5, subtract 2, and multiply by 3.
x = 10
x += 5
print("add 5:", x)
x -= 2
print("subtract 2:", x)
x *= 3
print("multiply by 3:", x)

