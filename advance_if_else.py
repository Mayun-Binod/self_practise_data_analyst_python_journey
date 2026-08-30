# Create a bank withdrawal system:
# Amount ≤ 0 → Invalid amount
# Amount > balance → Insufficient balance
# Amount > 25,000 → Daily limit exceeded
# Otherwise → Withdrawal successful
balance = 50000
withdraw = float(input("Enter withdrawal amount: "))
if withdraw <= 0:
    print("Invalid amount")
elif withdraw > balance:
    print("Insufficient balance")
elif withdraw > 25000:
    print("Daily limit exceeded")
else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)

# Create a login system using username and password:
# Both correct → Login successful
# Username correct but password wrong → Wrong password
# Both wrong → Invalid login
correct_username = "sandhya"
correct_password = "12345"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login successful")
elif username == correct_username and password != correct_password:
    print("Wrong password")
else:
    print("Invalid login")

# Create a student result system using marks and attendance:
# Marks ≥ 80 and attendance ≥ 75 → Excellent
# Marks ≥ 60 and attendance ≥ 75 → Good
# Marks ≥ 40 and attendance ≥ 75 → Pass
# Otherwise → Fail
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
if marks >= 80 and attendance >= 75:
    print("Excellent")
elif marks >= 60 and attendance >= 75:
    print("Good")
elif marks >= 40 and attendance >= 75:
    print("Pass")
else:
    print("Fail")

# Create an ATM menu:
# 1 → Check Balance
# 2 → Withdraw
# 3 → Deposit
# Any other number → Invalid option
option = int(input("Enter your option: "))
if option == 1:
    print("Your balance is:", balance)
elif option == 2:
    withdraw = float(input("Enter withdrawal amount: "))
    if withdraw <= 0:
        print("Invalid amount")
    elif withdraw > balance:
        print("Insufficient balance")
    else:
        balance = balance - withdraw
        print("Withdrawal successful")
        print("Remaining balance:", balance)
elif option == 3:
    deposit = float(input("Enter deposit amount: "))
    if deposit <= 0:
        print("Invalid deposit amount")
    else:
        balance = balance + deposit
        print("Deposit successful")
        print("New balance:", balance)
else:
    print("Invalid option")

# Take a person's age and income and check whether they are eligible for a loan.
age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
if age >= 18 and income >= 30000:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

# Create a bank account status system using balance and account status:
# Account inactive → Account is inactive
# Balance ≤ 0 → No available balance
# Balance > 100,000 → Premium account
# Otherwise → Normal account.
balance = float(input("Enter your balance: "))
status = input("Enter account status (active/inactive): ")
if status == "inactive":
    print("Account is inactive")
elif balance <= 0:
    print("No available balance")
elif balance > 100000:
    print("Premium account")
else:
    print("Normal account")

