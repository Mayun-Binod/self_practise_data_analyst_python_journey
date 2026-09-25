# Create a list of numbers and use a for loop to print numbers from 1–50 that are divisible by 5.
numbers = list(range(1, 51))
for number in numbers:
    if number % 5 == 0:
        print(number)

# Create a list of student marks and use a loop to print:
# Pass
# Fail
# for each student.
marks = [75, 35, 60, 40, 25]
for i in marks:
    if i >= 40:
        print("Pass")
    else:
        print("Fail")

# Create a dictionary:
# students = {
#     "Ram": 75,
#     "Sita": 35,
#     "Hari": 60,
#     "Gita": 40 }
# Print only students who passed.
students = {
    "Ram": 75,
    "Sita": 35,
    "Hari": 60,
    "Gita": 40
}
for name, marks in students.items():
    if marks >= 40:
        print(name, marks)

# Create a list of numbers and use continue to skip negative numbers.
numbers = [10, -5, 20, -10, 30, -2]
for number in numbers:
    if number < 0:
        continue
    print(number)

# Create a list of numbers and use break when you find the number 50. solve this
numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
    if number == 50:
        print("50 found")
        break
    print(number)