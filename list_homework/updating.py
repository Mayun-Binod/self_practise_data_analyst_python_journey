# Change the second item of a fruit list.
fruits = ["apple", "banana", "mango", "orange"]
fruits[1] = "grapes"
print(fruits)

# Change the last item using negative indexing.
fruits[-1] = "kiwi"
print(fruits)

# Replace the second and third items using slicing.
fruits[1:3] = ["orange", "watermelon"]
print(fruits)

# Replace the last two items with two new values.
fruits[-2:] = ["papaya", "pineapple"]
print(fruits)