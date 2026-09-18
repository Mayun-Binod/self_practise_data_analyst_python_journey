# Create a tuple containing three inner tuples.
numbers = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
print(numbers)

# Access the first item of the second inner tuple.
numbers = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
print(numbers[1][0])

# Access the last item of the third inner tuple.
numbers = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
print(numbers[2][-1])


# Use [2][0] on a nested tuple and find the output
numbers = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
print(numbers[2][0])

# Convert the outer tuple into a list.
numbers = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
new_list = list(numbers)
print(new_list)

#Convert one inner tuple into a list.
numbers = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
inner_list = list(numbers[0])
print(inner_list)