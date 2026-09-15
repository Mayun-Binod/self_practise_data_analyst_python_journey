# Delete the item at index 2.
fruits = ["apple", "banana", "mango", "orange"]
del fruits[2]
print(fruits)

# Delete the last item using negative indexing.
fruits = ["apple", "banana", "mango", "orange"]
del fruits[-1]
print(fruits)

# Delete a range of items using slicing with del.
numbers = [1, 2, 3, 4, 5, 6, 7]
del numbers[2:5]
print(numbers)

# Delete the entire list using del.
fruits = ["apple", "banana", "mango"]
del fruits
