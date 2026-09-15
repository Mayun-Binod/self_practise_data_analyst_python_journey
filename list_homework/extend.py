# Create two fruit lists and combine the second list into the first using extend().
fruits1 = ["apple", "banana"]
fruits2 = ["mango", "orange"]
fruits1.extend(fruits2)
print(fruits1)

# Extend a number list with another list containing 4 numbers.
numbers = [1, 2, 3]
numbers2 = [4, 5, 6, 7]
numbers.extend(numbers2)
print(numbers)

# Create three lists and use extend() to combine them.
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
list1.extend(list2)
list1.extend(list3)
print(list1)