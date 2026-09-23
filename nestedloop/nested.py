# ==========================================
# NESTED LOOP - PYTHON
# ==========================================


# 1. Basic Nested for Loop
for i in range(3):
    for j in range(3):
        print(i, j)


# 2. Print a 3 x 3 Pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# 3. Print Numbers in Rows
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()


# 4. Multiplication Table
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()


# 5. Nested Loop with List
fruits = ["Apple", "Mango", "Banana"]
colors = ["Red", "Yellow"]

for fruit in fruits:
    for color in colors:
        print(fruit, color)


# 6. Nested while Loop
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1


# 7. Nested Loop with break
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)


# 8. Nested Loop with continue
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)


# 9. Nested Loop with if-else
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            print("Same", end=" ")
        else:
            print("Different", end=" ")
    print()


# 10. Nested Loop - User Input
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print()