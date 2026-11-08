# ==========================================
# ENCAPSULATION - PRACTICE TASKS
# ==========================================

# Task 1: Student Age Validation
class Student:
    def __init__(self, age):
        self.__age = 0
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 <= age <= 60:
            self.__age = age
        else:
            print("Invalid age")


print("----- Task 1: Student -----")
student = Student(22)
print("Age:", student.age)
student.age = 65


# Task 2: Bank Account
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")


print("\n----- Task 2: Bank Account -----")
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Balance:", account.balance)


# Task 3: Employee Salary
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 15000:
            self.__salary = salary
        else:
            print("Salary should not be less than 15000")

    def display_details(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)


print("\n----- Task 3: Employee -----")
employee = Employee("Rahul", "IT", 25000)
employee.display_details()


# Task 4: Product Price
class Product:
    def __init__(self, price):
        self.__price = 0
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price")

    def display_details(self):
        print("Product Price:", self.__price)


print("\n----- Task 4: Product -----")
product = Product(500)
product.display_details()
product.price = -100


# Task 5: User Login System
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = ""
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) >= 8:
            self.__password = password
        else:
            print("Password must contain at least 8 characters")

    def login(self, username, password):
        if self.username == username and self.__password == password:
            print("Login successful")
        else:
            print("Login failed")


print("\n----- Task 5: User Login -----")
user = User("meryyesu", "password123")
user.login("meryyesu", "password123")
user.login("meryyesu", "wrongpass")
