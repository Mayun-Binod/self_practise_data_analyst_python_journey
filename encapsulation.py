# ==========================================
# Python OOP - Encapsulation
# ==========================================


# 1. Public Attribute
# ==========================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student = Student("Ram", 80)

print("Name:", student.name)
print("Marks:", student.marks)


# ==========================================
# 2. Protected Attribute
# ==========================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def show_age(self):
        print("Age:", self._age)


person = Person("Sita", 25)

print("\nName:", person.name)
person.show_age()


# ==========================================
# 3. Private Attribute
# ==========================================

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount("Hari", 50000)

print("\nAccount Holder:", account.name)

account.show_balance()

# Direct access is not allowed normally
# print(account.__balance)


# ==========================================
# 4. Private Attribute with Methods
# ==========================================

class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):

        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance


account = Account(10000)

print("\nInitial Balance:", account.get_balance())

account.deposit(5000)

print("After Deposit:", account.get_balance())

account.withdraw(3000)

print("After Withdrawal:", account.get_balance())


# ==========================================
# 5. Encapsulation with Getter and Setter
# ==========================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # Getter
    def get_salary(self):
        return self.__salary

    # Setter
    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be greater than 0.")


employee = Employee("Ram", 30000)

print("\nEmployee:", employee.name)
print("Salary:", employee.get_salary())

employee.set_salary(40000)

print("Updated Salary:", employee.get_salary())