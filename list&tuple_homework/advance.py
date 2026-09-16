# Create a list of student tuples containing name and marks. Use a loop to print each student's name and marks.
students = [("sandhya", 80),("Sita", 90),("nisana", 75),("sunita", 85)]
for name, marks in students:
    print("Name:", name)
    print("Marks:", marks)

# Create a list of tuples containing product name and price. Calculate the total price using a loop.
products = [
    ("Laptop", 80000),
    ("Mouse", 15000),
    ("Keyboard", 25000),
    ("Monitor", 25000)
]
total = 0
for product, price in products:
    total += price
print("Total Price:", total)

# Create a list of tuples and find the tuple containing the highest number.
numbers = [(10, 20),(30, 15),(25, 40),(50, 10)]
highest = numbers[0]
for i  in numbers:
    if max(i) > max(highest):
        highest = i
print(highest)

# Create a list of numbers and create a new list containing only unique values without using set().
numbers = [10, 20, 30, 40, 50]
unique_values = []
for i in numbers:
    if i not in unique_values:
        unique_values.append(i)
print(unique_values)

# Create a nested list and access, update, and delete specific items inside the nested list.
students = [["sandhya", 80], ["prakriti", 90], ["sunita", 70]]
print(students[0][0])
students[1][1] = 80
del students[2]
print(students)

# Create a list of tuples and sort it based on the second value of each tuple.
students = [ ("sandhya", 80), ("prakriti", 70), ("nisana", 90), ("Gita", 85)]
students.sort(key=lambda student: student[1])
print(students)

# Create two lists and use zip() to combine their corresponding values into tuples.
names = ["binod", "Sita", "nisana"]
marks = [80, 90, 75]
result = list(zip(names, marks))
print(result)

# Use tuple unpacking with a for loop to process a list of tuples.
students = [ ("sandhya", 80),("Sita", 90),("nisana", 75)]
for name, marks in students:
    print(name, marks)

# Create a list of student records using tuples. Find the student with the highest marks. solve this
students = [("sandhya", 80),("sunita", 95),("nisana", 75),("Gita", 88)]
highest_student = students[0]
for student in students:
    if student[1] > highest_student[1]:
        highest_student = student

print("Student:", highest_student[0])
print("Marks:", highest_student[1])
