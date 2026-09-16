# Create a list of numbers, remove all duplicate values, and create a new list.
numbers = [10, 20, 30, 40, 50,]
number = []
for i in numbers:
    if i not in number:
        number.append(i)
        print(number)

# Create a list of student marks and calculate the total and average using a loop.
marks = [80, 90, 60, 50]
total = 0
for i in marks:
    total += i
average = total / len(marks)
print("Total:", total)
print("Average:", average)

# Create a list of numbers and separate the even and odd numbers into two different lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []
odd_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("Even:", even_numbers)
print("Odd:", odd_numbers)

# Create a list of names and print each name together with its index.
names = ["sandhya", "nisana", "sunita", "Gita"]
for index, name in enumerate(names):
    print(index, name)

# Create a list of numbers and count how many times each number appears.
numbers = [1, 2, 2, 3, 3, 3, 4, 4]
count = {}
for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1
print(count)

# Create two lists and find the common items between them.
list1 =[1, 2, 3, 4, 5]
list2 =[1, 2, 3, 4, 5]
common =[]
for i in list1:
    if i in list2:
        common.append(i)
print(common)

# Convert a list into a tuple.
numbers = [1, 2, 3, 4, 5]
numbers_tuple = tuple(numbers)
print(numbers_tuple)

# Convert a tuple into a list.
numbers = (1, 2, 3, 4, 5)
numbers_list = list(numbers)
print(numbers_list)

# Create a tuple, convert it into a list, modify the list, and convert it back into a tuple.
numbers = (10, 20, 30, 40)
numbers_list = list(numbers)
numbers_list.append(50)
numbers = tuple(numbers_list)
print(numbers)




