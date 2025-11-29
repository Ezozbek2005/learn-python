# 1-misol

# import math

# class Circle:
#     def __init__(self, radius):
#         if radius <= 0:
#             raise ValueError("Radius 0 dan katta bo'lishi kerak!")
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius


# # --- Foydalanuvchidan radius olish ---
# try:
#     r = float(input("Doira radiusini kiriting: "))
#     c = Circle(r)

#     print("Yuzi:", c.area())
#     print("Perimetri:", c.perimeter())

# except ValueError as e:
#     print("Xatolik:", e)

# # 2-misol
# from datetime import datetime, date

# class Person:
#     def __init__(self, name, country, birth_date):
#         """
#         birth_date: 'YYYY-MM-DD' formatida
#         """
#         self._name = name
#         self._country = country
#         self._birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

#     def get_name(self):
#         return self._name

#     def get_country(self):
#         return self._country

#     def get_age(self):
#         today = date(2025, 11, 27)  # misol uchun hozirgi sana
#         age = today.year - self._birth_date.year
#         if (today.month, today.day) < (self._birth_date.month, self._birth_date.day):
#             age -= 1
#         return age


# # --- Foydalanuvchidan ma’lumot olish ---
# name = input("Ismingizni kiriting: ")
# country = input("Davlatingizni kiriting: ")
# birth_date = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")

# # Person obyektini yaratish
# person = Person(name, country, birth_date)

# # Metodlar orqali ma’lumotlarni chiqarish
# print("\n--- Ma’lumotlar ---")
# print("Ismi:", person.get_name())
# print("Davlati:", person.get_country())
# print("Yoshi:", person.get_age())

# 3-misol 1-usul
# class Calculator:
#     def __init__(self):
#         pass  # Hozircha hech qanday atributga ehtiyoj yo'q

#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             return "Error: 0 ga bo'lish mumkin emas!"
#         return a / b


# # --- Misol ishlatish ---
# calc = Calculator()

# print("3 + 5 =", calc.add(3, 5))
# print("10 - 4 =", calc.subtract(10, 4))
# print("6 * 7 =", calc.multiply(6, 7))
# print("20 / 5 =", calc.divide(20, 5))
# print("10 / 0 =", calc.divide(10, 0))

# 3-misol 2-usul
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             return "Error: 0 ga bo'lish mumkin emas!"
#         return a / b


 
# calc = Calculator()

# print("Simple Calculator")
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))

# print("Amalni tanlang: +, -, *, /")
# operation = input("Tanlangan amal: ")

# if operation == '+':
#     result = calc.add(a, b)
# elif operation == '-':
#     result = calc.subtract(a, b)
# elif operation == '*':
#     result = calc.multiply(a, b)
# elif operation == '/':
#     result = calc.divide(a, b)
# else:
#     result = "Noto'g'ri amal tanlandi!"

# print("Natija:", result)


# 4-misol

# import math

# class Shape:
#     def area(self):
#         pass
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius**2
#     def perimeter(self):
#         return 2 * math.pi * self.radius

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side**2
#     def perimeter(self):
#         return 4 * self.side

# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c
#     def perimeter(self):
#         return self.a + self.b + self.c
#     def area(self):
#         s = self.perimeter()/2
#         return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

# # Misol
# circle = Circle(5)
# square = Square(4)
# triangle = Triangle(3,4,5)

# print("Circle area:", circle.area(), "perimeter:", circle.perimeter())
# print("Square area:", square.area(), "perimeter:", square.perimeter())
# print("Triangle area:", triangle.area(), "perimeter:", triangle.perimeter())


# 5-misol

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert(self.root, data)

#     def _insert(self, node, data):
#         if data < node.data:
#             if node.left is None:
#                 node.left = Node(data)
#             else:
#                 self._insert(node.left, data)
#         else:
#             if node.right is None:
#                 node.right = Node(data)
#             else:
#                 self._insert(node.right, data)

#     def search(self, data):
#         return self._search(self.root, data)

#     def _search(self, node, data):
#         if node is None:
#             return False
#         if node.data == data:
#             return True
#         elif data < node.data:
#             return self._search(node.left, data)
#         else:
#             return self._search(node.right, data)

# # Misol
# bst = BST()
# bst.insert(10)
# bst.insert(5)
# bst.insert(15)
# print("Search 15:", bst.search(15))
# print("Search 7:", bst.search(7))

# # 6-misol
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if self.items:
#             return self.items.pop()
#         return "Stack bo'sh!"

# # Misol
# stack = Stack()
# stack.push(10)
# stack.push(20)
# print("Pop:", stack.pop())
# print("Pop:", stack.pop())
# print("Pop:", stack.pop())


#7-misol
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete(self, key):
#         temp = self.head
#         prev = None
#         while temp:
#             if temp.data == key:
#                 if prev:
#                     prev.next = temp.next
#                 else:
#                     self.head = temp.next
#                 return
#             prev = temp
#             temp = temp.next

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# # Misol
# ll = LinkedList()
# ll.insert(10)
# ll.insert(20)
# ll.insert(30)
# ll.display()
# ll.delete(20)
# ll.display()

# 8-misol
# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, name, price):
#         self.items.append({"name": name, "price": price})

#     def remove_item(self, name):
#         self.items = [item for item in self.items if item["name"] != name]

#     def total_price(self):
#         return sum(item["price"] for item in self.items)

# # Misol
# cart = ShoppingCart()
# cart.add_item("Apple", 3)
# cart.add_item("Banana", 2)
# cart.remove_item("Apple")
# print("Total:", cart.total_price())


# 9 -misol
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if self.items:
#             return self.items.pop()
#         return "Stack bo'sh!"

#     def display(self):
#         print("Stack:", self.items)

# # Misol
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.display()
# stack.pop()
# stack.display()

# 10-misol
# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if self.items:
#             return self.items.pop(0)
#         return "Queue bo'sh!"

#     def display(self):
#         print("Queue:", self.items)

# # Misol
# q = Queue()
# q.enqueue(5)
# q.enqueue(10)
# q.display()
# q.dequeue()
# q.display()

# 11-misol
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Balance: {self.balance}")
        else:
            print("Insufficient funds!")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        self.accounts[name] = BankAccount(name, balance)
        print(f"Account created for {name}.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)
        else:
            print("Account not found!")

    def withdraw(self, name, amount):
        if name in self.accounts:
            self.accounts[name].withdraw(amount)
        else:
            print("Account not found!")

# Misol
bank = Bank()
bank.create_account("Ezozbek", 100)
bank.deposit("Ezozbek", 50)
bank.withdraw("Ezozbek", 120)
bank.withdraw("Ezozbek", 50)

