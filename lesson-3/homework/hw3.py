# 1. Create and Access List Elements
print("1. SHART: 5 ta meva listi tuz va 3-mevani chiqar.")
fruits = ["apple", "banana", "orange", "grape", "mango"]
print("Natija:", fruits[2])
print()

# ------------------------------------------------------

# 2. Concatenate Two Lists
print("2. SHART: 2 ta listni bitta listga qo'sh.")
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print("Natija:", c)
print()

# ------------------------------------------------------

# 3. Extract Elements from a List
print("3. SHART: Listdan birinchi, o'rta va oxirgi elementlarni ajrat.")

nums = [10, 20, 30, 40, 50]

a = len(nums) // 2   

new_list = [nums[0], nums[a], nums[-1]]
print("Natija:", new_list)
print()

# ------------------------------------------------------

# 4. Convert List to Tuple
print("4. SHART: 5 ta film listini tuplega aylantir.")
movies = ["Inception", "Avatar", "Titanic", "Matrix", "Shrek"]
movies_tuple = tuple(movies)
print("Natija:", movies_tuple)
print()

# ------------------------------------------------------

# 5. Check Element in a List
print("5. SHART: 'Paris' shahri listda bormi?")
cities = ["Paris", "London", "Dubai", "Tokyo"]
print("Natija:", "Paris" in cities)
print()

# ------------------------------------------------------

# 6. Duplicate a List Without Using Loops
print("6. SHART: Listni siklsiz 2 martaga ko'paytir.")
nums2 = [1, 2, 3]
dup = nums2 * 2
print("Natija:", dup)
print()

# ------------------------------------------------------

# 7. Swap First and Last Elements
print("7. SHART: Listning birinchi va oxirgi elementlarini almashtir.")
numbers = [10, 20, 30, 40]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("Natija:", numbers)
print()

# ------------------------------------------------------

# 8. Slice a Tuple
print("8. SHART: 1 dan 10 gacha tuple yarat va 3-7 indekslarni chiqar.")
t = (1,2,3,4,5,6,7,8,9,10)
print("Natija:", t[3:8])
print()

# ------------------------------------------------------

# 9. Count Occurrences in a List
print("9. SHART: 'blue' nechta marta uchraydi?")
colors = ["blue", "red", "blue", "green", "blue"]
print("Natija:", colors.count("blue"))
print()

# ------------------------------------------------------

# 10. Find Index in Tuple
print("10. SHART: Tuple ichidan 'lion' indeksini top.")
animals = ("cat", "dog", "lion", "tiger")
print("Natija:", animals.index("lion"))
print()

# ------------------------------------------------------

# 11. Merge Two Tuples
print("11. SHART: 2 ta tuple'ni birlashtir.")
a1 = (1, 2, 3)
b1 = (4, 5, 6)
merged = a1 + b1
print("Natija:", merged)
print()

# ------------------------------------------------------

# 12. Length of List and Tuple
print("12. SHART: List va tuple uzunligini top.")
my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
print("List uzunligi:", len(my_list))
print("Tuple uzunligi:", len(my_tuple))
print()

# ------------------------------------------------------

# 13. Convert Tuple to List
print("13. SHART: Tuple'ni listga aylantir.")
t2 = (5, 10, 15, 20, 25)
lst = list(t2)
print("Natija:", lst)
print()

# ------------------------------------------------------

# 14. Max and Min in Tuple
print("14. SHART: Tuple ichidagi eng katta va eng kichik sonni top.")
nums3 = (10, 50, 30, 5, 90)
print("Max:", max(nums3))
print("Min:", min(nums3))
print()

# ------------------------------------------------------

# 15. Reverse a Tuple
print("15. SHART: Tuple'ni teskari chiqar.")
words = ("hello", "world", "python")
print("Natija:", words[::-1])
print()
