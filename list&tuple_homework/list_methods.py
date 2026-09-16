# Create a list and add an item using append().
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)

# Insert an item at a specific position using insert().
fruits = ["apple", "banana", "mango"]
fruits.insert(1, "orange")
print(fruits)

# Create two lists and combine them using extend().
fruits1 = ["apple", "banana"]
fruits2 = ["mango", "orange"]
fruits1.extend(fruits2)
print(fruits1)

# Remove a specific item using remove().
fruits = ["apple", "banana", "mango", "orange"]
fruits.remove("mango")
print(fruits)

# Remove an item at a specific index using pop().
numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(numbers)

# Remove all items using clear().
fruits = ["apple", "banana", "mango"]
fruits.clear()
print(fruits)

# Delete a specific item using del.
fruits = ["apple", "banana", "mango", "orange"]
del fruits[2]
print(fruits)

# Delete a range of items using del and slicing.
numbers = [10, 20, 30, 40, 50, 60]
del numbers[1:4]
print(numbers)

# Sort a list in ascending order using sort().
numbers = [50, 20, 80, 10, 40]
numbers.sort()
print(numbers)

# Sort a list in descending order using sort().
numbers = [50, 20, 80, 10, 40]
numbers.sort(reverse=True)
print(numbers)

# Reverse a list using reverse().
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

# Find the number of items using len().
fruits = ["apple", "banana", "mango", "orange"]
print(len(fruits))

# Find how many times a particular value occurs using count().
numbers = [10, 20, 10, 30, 20, 40]
print(numbers.count(10))

# Find the position of a particular value using index().
fruits = ["apple", "banana", "mango", "orange"]
print(fruits.index("mango"))

# Create a copy of a list using copy() and modify the copied list.
fruits = ["apple", "banana", "mango"]
fruits1 = fruits.copy()
fruits1.append("orange")
print(fruits)
print(fruits1)


