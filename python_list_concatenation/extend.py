# Create two lists of fruits and add all items from the second list to the first using extend().
fruits1 = ["apple", "banana", "orange"]
fruits2 = ["mango", "grapes", "papaya"]
fruits1.extend(fruits2)
print(fruits1)

# Create a list of numbers and extend it with another list containing 5 numbers.
numbers1 = [10, 20, 30]
numbers2 = [40, 50, 60, 70, 80]
numbers1.extend(numbers2)
print(numbers1)

# Create three lists of names and use extend() to combine them.
names1 = ["Ram", "Hari"]
names2 = ["Sita", "Gita"]
names3 = ["Shyam", "Mina"]
names1.extend(names2)
names1.extend(names3)
print(names1)

# Create an empty list and use extend() to add items from two different lists.
list1 = ["apple", "banana"]
list2 = ["mango", "orange"]
result = []
result.extend(list1)
result.extend(list2)
print(result)


