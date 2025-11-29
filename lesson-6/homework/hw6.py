# ===============================
# HOMEWORK SOLUTIONS — FULL FILE
# ===============================


# ========================================
# 1. Modify String With Underscores
# ========================================

def add_underscores(txt):
    vowels = "aeiou"
    result = ""
    count = 0  # 3 ta harf sanash

    for i in range(len(txt)):
        result += txt[i]
        count += 1

        if count == 3:
            if txt[i] not in vowels and i != len(txt) - 1:
                result += "_"
            count = 0

    return result


print("=== 1. Modify String With Underscores ===")
print(add_underscores("hello"))
print(add_underscores("assalom"))
print(add_underscores("abcabcabcdeabcdefabcdefg"))
print("\n")


# ========================================
# 2. INTEGER SQUARES
# ========================================

print("=== 2. Integer Squares ===")
n = int(input("Enter n: "))
for i in range(n):
    print(i * i)
print("\n")


# ========================================
# 3. LOOP EXERCISES
# ========================================

print("=== 3. Loop Exercises ===")

# Exercise 1 — first 10 natural numbers
print("\nExercise 1:")
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2 — pattern
print("\nExercise 2:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 3 — sum 1..n
print("\nExercise 3:")
n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)

# Exercise 4 — multiplication table
print("\nExercise 4:")
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i)

# Exercise 5 — display numbers with conditions
print("\nExercise 5:")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num == 525:
        break
    if num % 5 == 0 and num < 500:
        print(num)

# Exercise 6 — count digits
print("\nExercise 6:")
num = input("Enter a number: ")
print("Digits:", len(num))

# Exercise 7 — reverse pattern
print("\nExercise 7:")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8 — reverse list display
print("\nExercise 8:")
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])

# Exercise 9 — -10 to -1
print("\nExercise 9:")
for i in range(-10, 0):
    print(i)

# Exercise 10 — Done message
print("\nExercise 10:")
for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11 — prime numbers
print("\nExercise 11:")
print("Prime numbers between 25 and 50:")
for num in range(25, 51):
    if num < 2:
        continue
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            break
    else:
        print(num)

# Exercise 12 — Fibonacci
print("\nExercise 12:")
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end="  ")
    a, b = b, a + b

# Exercise 13 — factorial
print("\nExercise 13:")
n = int(input("\nEnter number for factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! =", fact)


# ========================================
# 4. Uncommon Elements Between Lists
# ========================================

print("\n=== 4. Uncommon Elements ===")

def uncommon(list1, list2):
    result = []

    for x in list1:
        if x not in list2:
            result.append(x)

    for y in list2:
        if y not in list1:
            result.append(y)

    return result


print(uncommon([1, 1, 2], [2, 3, 4]))
print(uncommon([1, 2, 3], [4, 5, 6]))
print(uncommon([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))
