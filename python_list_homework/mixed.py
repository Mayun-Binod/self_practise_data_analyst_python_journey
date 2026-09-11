# Create a list of 8 fruits. Access the third item, update the fifth item, slice the first four items, find the index of "apple", and delete the last item.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango", "grape", "papaya"]
print(fruits[2])
fruits[4] = "watermelon"
print(fruits[:4])
print(fruits.index("apple"))
del fruits[-1]
print(fruits)

# Create a list of 10 numbers. Access the first and last numbers, update the third number, print the middle five numbers using slicing, find the index of 50, and delete the number at index 2.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[0])
print(numbers[-1])
numbers[2] = 35
print(numbers[3:8])
print(numbers.index(50))
del numbers[2]
print(numbers)

# Create a list of 7 student names. Access two names, update two names, print the last three names using slicing, find the index of one name, and delete one name using del.
students = ["Ram", "Sita", "Hari", "Gita", "Rita", "Shyam", "Mina"]
print(students[1])
print(students[4])
students[2] = "Binod"
students[5] = "sandhya"
print(students[-3:])
print(students.index("Binod"))
del students[0]
print(students)

# Create a list of 10 numbers and perform access → update → slice → index → delete operations one after another. solve this
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Access
print(numbers[2])
# Update
numbers[4] = 500
print(numbers)
# Slice
print(numbers[2:7])
# Index
print(numbers.index(50))
# Delete
del numbers[3]
print(numbers)
