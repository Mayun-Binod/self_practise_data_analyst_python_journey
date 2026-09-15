# Create a list of 10 numbers and perform indexing, slicing, updating, del****, append()****, pop()****, and sort().
fruits = ["apple", "banana", "mango", "orange", "grapes", "kiwi", "papaya", "watermelon"]

# Access
print(fruits[2])

# Update
fruits[2] = "pineapple"
print(fruits)

# append()
fruits.append("guava")
print(fruits)

# insert()
fruits.insert(2, "cherry")
print(fruits)

# extend()
fruits.extend(["peach", "plum"])
print(fruits)

# remove()
fruits.remove("banana")
print(fruits)

# pop()
fruits.pop()
print(fruits)

# sort()
fruits.sort()
print(fruits)

# reverse()
fruits.reverse()
print(fruits)

# len()
print(len(fruits))

# Create two lists, concatenate them using +, then use append(), insert(), extend(), remove(), and pop() on the resulting list.
list1 = ["apple", "banana", "mango"]
list2 = ["orange", "grapes", "kiwi"]
result = list1 + list2

print(result)

result.append("papaya")
print(result)

result.insert(2, "cherry")
print(result)

result.extend(["peach", "plum"])
print(result)

result.remove("banana")
print(result)

result.pop()
print(result)

# Create a list containing duplicate values and practice count()****, index()****, remove()****, sort()****, and reverse().
numbers = [30, 10, 20, 10, 40, 10, 50, 20]

# count()
print(numbers.count(10))

# index()
print(numbers.index(20))

# remove()
numbers.remove(10)
print(numbers)

# sort()
numbers.sort()
print(numbers)

# reverse()
numbers.reverse()
print(numbers)


# Create an empty list and use append() and extend() to build a list of 10 numbers. Then sort, reverse, and find its length. solve this
numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)

numbers.extend([50, 60, 70, 80, 90, 100])

print("List:", numbers)

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

print("Length:", len(numbers))
