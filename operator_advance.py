# Create a bank withdrawal system using arithmetic, comparison, and logical operators.
balance = float(input("Enter your balance: "))
withdraw = float(input("Enter withdrawal amount: "))
if withdraw > 0 and withdraw <= balance:
    balance -= withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Invalid withdrawal amount")

# Create a login system that checks username and password using and.
correct_username = "admin"
correct_password = "1234"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")

# Create a student grading system using comparison and logical operators.
marks = float(input("Enter marks: "))
if marks >= 80 and marks <= 100:
    print("Grade A+")
elif marks >= 70 and marks < 80:
    print("Grade A")
elif marks >= 60 and marks < 70:
    print("Grade B+")
elif marks >= 40 and marks < 60:
    print("Grade B")
elif marks >= 0 and marks < 40:
    print("Grade C")
else:
    print("Invalid marks")  

# Create a shopping discount system:
# Amount ≥ 10,000 → 20% discount
# Amount ≥ 5,000 → 10% discount
# Amount ≥ 2,000 → 5% discount
# Otherwise → No discount
amount = float(input("Enter shopping amount: "))
if amount >= 10000:
    discount = amount * 20 / 100
elif amount >= 5000:
    discount = amount * 10 / 100
elif amount >= 2000:
    discount = amount * 5 / 100
else:
    discount = 0
final_amount = amount - discount
print("Original amount:", amount)
print("Discount:", discount)
print("Final amount:", final_amount)

# Take three numbers and find the largest number using comparison and logical operators.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("Largest number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number:", num2)
elif num3 >= num1 and num3 >= num2:
    print("Largest number:", num3)
else:
    print("Largest number:")

# Create a course enrollment system. Check whether the selected course is in the available course list and whether the student's marks are at least 60.
courses = ["Python", "SQL", "Power BI", "Excel"]
course = "SQL"
marks = 75
if course in courses and marks >= 60:
    print("You can enroll in the course")
else:
    print("You cannot enroll in the course")

# Create an employee bonus system using salary, years of experience, and performance:
# Experience ≥ 5 years and performance ≥ 80 → High bonus
# Experience ≥ 3 years and performance ≥ 60 → Medium bonus
# Otherwise → No bonus
salary = 60000
experience = 6
performance = 85
if experience >= 5 and performance >= 80:
    print("High bonus")
elif experience >= 3 and performance >= 60:
    print("Medium bonus")
else:
    print("No bonus")

# Create a complete bank transaction system using:
# +, -, *, /, %
# =, +=, -=
# ==, !=, >, <, >=, <=
# and, or, not
# in, not in
accounts = [1001, 1002, 1003]
account = 1001
balance = 50000
if account in accounts:
    print("Account found")
    # Arithmetic operators
    deposit = 10000
    withdrawal = 5000
    balance = balance + deposit
    balance = balance - withdrawal
    print("Balance:", balance)
    # += operator
    balance += 2000
    print("After +=:", balance)
    # -= operator
    balance -= 1000
    print("After -=:", balance)
    # * operator
    print("Double balance:", balance * 2)
    # / operator
    print("Half balance:", balance / 2)
    # % operator
    print("Remainder:", balance % 3)
    # Comparison operators
    print(balance == 56000)
    print(balance != 0)
    print(balance > 50000)
    print(balance < 100000)
    print(balance >= 50000)
    print(balance <= 100000)
    # Logical operators
    if balance > 0 and balance >= 50000:
        print("Account has sufficient balance")
    if balance == 56000 or balance == 50000:
        print("Balance matches a valid amount")
    if not balance < 0:
        print("Balance is not negative")
    # not in
    blocked_accounts = [2001, 2002, 2003]
    if account not in blocked_accounts:
        print("Account is not blocked")
else:
    print("Account does not exist")

