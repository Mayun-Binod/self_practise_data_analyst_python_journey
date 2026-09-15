# Create a list and make a separate copy using copy().
fruits = ["apple", "banana", "mango"]
fruits1 = fruits.copy()
print(fruits)
print(fruits1)

# Add a new item to the copied list and check whether the original list changes.
fruits = ["apple", "banana", "mango"]
new_fruits = fruits.copy()
new_fruits.append("orange")
print("Original:", fruits)
print("Copied:", new_fruits)

# Find the index of a specific fruit using index().
fruits = ["apple", "banana", "mango", "orange"]
fruits1 = fruits.index("mango")
print(fruits1)

# Create a list with duplicate numbers and count a number using count().
numbers = [10, 20, 10, 30, 10, 40]
result = numbers.count(10)
print(result)

# Find the total number of items using len().
fruits = ["apple", "banana", "mango", "orange"]
total = len(fruits)
print(total)
