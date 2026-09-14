# Create a list of 8 fruits and find the number of items using len().
fruits = ["apple", "banana", "orange", "mango", "grapes", "papaya", "kiwi", "watermelon"]
print(len(fruits))

# Create a list of student names and find how many students are in the list.
students = ["Ram", "Hari", "Sita", "Gita", "Shyam"]
print(len(students))

# Create a list of numbers and use len() to find the total number of numbers.
numbers = [10, 20, 30, 40, 50, 60]
print(len(numbers))

# Take 5 names from the user, store them in a list, and find the length of the list. solve this
names = []
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
name3 = input("Enter third name: ")
name4 = input("Enter fourth name: ")
name5 = input("Enter fifth name: ")

names.append(name1)
names.append(name2)
names.append(name3)
names.append(name4)
names.append(name5)

print(names)
print("Number of names:", len(names))