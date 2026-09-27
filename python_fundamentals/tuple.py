# Create a tuple of 5 numbers and print each element using a loop.
numbers = (10, 20, 30, 40, 50)
for number in numbers:
    print(number)

# Find the largest and smallest number in a tuple.
numbers = (10, 25, 5, 40, 15)
largest = max(numbers)
smallest = min(numbers)
print(largest)
print(smallest)

# Unpack a tuple into separate variables.
person = ("sandhya", 19, "Kathmandu")
name, age, city = person
print(name,age, city)