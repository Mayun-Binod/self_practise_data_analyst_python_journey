# Create a list of fruits and change the second item.
fruits = ["apple", "banana", "orange", "mango"]
fruits[1] = "grapes"
print(fruits)

# Change the last item using negative indexing.
fruits = ["apple", "banana", "mango", "orange"]
fruits[-1] = "watermelon"
print(fruits)

# Replace three items using slicing.
fruits = ["apple", "banana", "mango", "orange", "grapes"]
fruits[1:4] = ["kiwi", "melon", "papaya"]
print(fruits)

# Replace two items with four new items.
fruits = ["apple", "banana", "mango", "orange"]
fruits[1:3] = ["kiwi", "melon", "papaya", "grapes"]
print(fruits)

# Replace four items with two new items.
fruits = ["apple", "banana", "mango", "orange", "grapes"]
fruits[0:4] = ["kiwi", "melon"]
print(fruits)


