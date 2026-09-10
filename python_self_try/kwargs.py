# Create a function using **kwargs that prints the complete dictionary.
def print_dictionary(**kwargs):
    print(kwargs)
print_dictionary(name="sandhya", age=19, city="Kathmandu")

# Create a function using **kwargs that prints only the keys.
def print_keys(**kwargs):
    for key in kwargs:
        print(key)
print_keys(name="sandhya", age=19, city="Kathmandu")

# Create a function using **kwargs that prints only the values.
def print_values(**kwargs):
    for value in kwargs.values():
        print(value)
print_values(name="sandhya", age=19, city="Kathmandu")

# Create a function using **kwargs that counts the number of arguments.
def count_arguments(**kwargs):
    count = 0
    for key in kwargs:
        count = count + 1
    return count
print(count_arguments(name="sandhya", age=19, city="Kathmandu"))

# Create a function using **kwargs that prints:
# name = Binod
# age = 25
# city = Kathmandu
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)
print_details(name="Binod", age=25, city="Kathmandu")

# Create a function using **kwargs that searches for a given key.
def search_key(search, **kwargs):
    if search in kwargs:
        return kwargs[search]
    else:
        return "Key not found"
print(search_key("age", name="Binod", age=25, city="Kathmandu"))

# Create a function using **kwargs that calculates the sum of all numeric values. solve this
def numeric_sum(**kwargs):
    total = 0
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total = total + value
    return total
print(numeric_sum(name="Binod", age=25, salary=50000, city="Kathmandu"))

