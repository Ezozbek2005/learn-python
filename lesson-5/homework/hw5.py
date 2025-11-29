# ===============================
# HOMEWORK: Leap Year, Conditional, Even Numbers
# ===============================

# 1️⃣ Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")

print("\n")

# 2️⃣ Conditional Statements
n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

print("\n")

# 3️⃣ Even Numbers Between Two Numbers
a = int(input("Enter start number a: "))
b = int(input("Enter end number b: "))

# Odda bo'lsa 1 qo'shish
start = a if a % 2 == 0 else a + 1

# Juft sonlar ro'yxati
evens = list(range(start, b+1, 2))
print("Even numbers between a and b:", evens)


# ===============================
# HOMEWORK: Leap Year, Conditional, Even Numbers
# ===============================

# 1️⃣ Leap Year
print("=== 1. Leap Year Check ===")

def is_leap(year):
    """
    Tekshiradi, yil leap year (kabiy yil) yoki yo'q.
    Shart:
    - 4 ga bo‘linadi va 100 ga bo‘linmaydi
    - yoki 400 ga bo‘linadi
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    year = int(input("Enter a year: "))
    if is_leap(year):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")
except ValueError:
    print("Invalid input! Please enter an integer.")

print("\n=== 2. Conditional Statements Exercise ===")

# 2️⃣ Conditional Statements
n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

print("\n=== 3. Even Numbers Between Two Numbers ===")

# 3️⃣ Even Numbers Between a and b
a = int(input("Enter start number a: "))
b = int(input("Enter end number b: "))

# Solution 1: If-Else (sodda)
start = a if a % 2 == 0 else a + 1
evens_if = list(range(start, b+1, 2))
print("Solution 1 (with if-else):", evens_if)

# Solution 2: Without if-else (conditional ishlatmasdan)
# math formula yordamida: a + (a % 2) → agar a toq bo‘lsa 1 qo‘shiladi, juft bo‘lsa 0
evens_no_if = list(range(a + (a % 2), b+1, 2))
print("Solution 2 (without if-else):", evens_no_if)
