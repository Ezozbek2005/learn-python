 # ==========================
# DICTIONARY EXERCISES
# ==========================

# 1. Sort a Dictionary by Value
print("1. SHART: Dictionary qiymatlari bo'yicha kichikdan kattaga va kattadan kichikka sort qil.")
data = {"a": 30, "b": 10, "c": 20}

asc = dict(sorted(data.items(), key=lambda x: x[1]))
print("Ascending:", asc)

desc = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
print("Descending:", desc)
print()

# ------------------------------------------------------

# 2. Add a Key to a Dictionary
print("2. SHART: Dictionaryga yangi key qo'sh.")
d = {0: 10, 1: 20}
d[2] = 30
print(d)
print()

# ------------------------------------------------------

# 3. Concatenate Multiple Dictionaries
print("3. SHART: Uchta dictionaryni birlashtir.")
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)
print(new_dic)
print()

# ------------------------------------------------------

# 4. Generate a Dictionary with Squares (1 to n)
print("4. SHART: 1 dan n gacha kvadrat dictionary yarat.")
n = 5
d = {}
for x in range(1, n + 1):
    d[x] = x * x
print(d)
print()

# ------------------------------------------------------

# 5. Dictionary of Squares (1 to 15)
print("5. SHART: 1 dan 15 gacha kvadrat dictionary yarat.")
d = {}
for x in range(1, 15 + 1):
    d[x] = x * x
print(d)
print()

# ==========================
# SET EXERCISES
# ==========================

# 1. Create a Set
print("1. SHART: Set yarat.")
my_set = {1, 2, 3, 4}
print(my_set)
print()

# ------------------------------------------------------

# 2. Iterate Over a Set
print("2. SHART: Set elementlari ustida yurish.")
for x in my_set:
    print(x)
print()

# ------------------------------------------------------

# 3. Add Member(s) to a Set
print("3. SHART: Setga element qo'sh.")
my_set.add(5)
my_set.add(6)
print(my_set)
print()

# ------------------------------------------------------

# 4. Remove Item(s) from a Set
print("4. SHART: Setdan element o'chir.")
my_set.remove(4)  # bor bo‘lsa o‘chiradi
print(my_set)
print()

# ------------------------------------------------------

# 5. Remove an Item if Present in the Set
print("5. SHART: Agar element setda bo'lsa o'chir.")
my_set.discard(6)  # bor bo‘lsa o‘chiradi, yo‘q bo‘lsa xato bermaydi
print(my_set)
print()
