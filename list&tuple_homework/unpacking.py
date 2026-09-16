# Unpack a tuple into separate variables.
fruits = ("apple", "banana", "cherry",)
name, fruit, green = fruits 
print(name)
print(fruit)
print(green)

# Create a tuple containing five values and unpack all five values.
numbers = (10, 20, 30, 40, 50)
a, b, c, d, e = numbers
print(a)
print(b)
print(c)
print(d)
print(e)

# Use * during tuple unpacking to collect multiple remaining values.
fruits = ("apple", "banana", "cherry")
multiple = fruits*2
print(multiple)

# Swap the values of two variables using tuple unpacking.
a = 10
b = 20
a, b = b, a
print(a)
print(b)


