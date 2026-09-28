# Ask the user to enter a number. Use try and except to handle invalid input.
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number.")
    
# Ask the user to enter two numbers and divide the first number by the second. Handle the situation when the second number is zero.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError as b:
    print("Please enter valid numbers", b)
except Exception as e:
    print("Something went wrong", e)

# Create a list of five numbers. Ask the user to enter an index and display the corresponding number. Handle an invalid index.
numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter an index: "))
    print(numbers[index])
except IndexError:
    print("Invalid index")
except ValueError:
    print("Please enter a valid number")

# Create a dictionary containing a student's name, age, and grade. Ask the user to enter a key and display its value. Handle a key that does not exist.
student = {
    "name": "sandhya",
    "age": 19,
    "grade": "A"
}
try:
    key = input("Enter a key: ")
    print("Value:", student[key])
except Exception as e:
    print("That key does not exist.")

# Ask the user to enter their age. If th60e user enters something other than a number, display a suitable error message instead of allowing the program to crash. solve this
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Invalid age")