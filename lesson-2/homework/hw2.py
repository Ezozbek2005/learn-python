 # ================================
# 1. AGE CALCULATOR
# Sharti: Foydalanuvchidan ism va tug'ilgan yil so'rang,
#         yoshini hisoblab chiqaring.
# ================================
name = input(" Ismingiz: ")
year = int(input("Tug'ilgan yilingiz: "))
age = 2025 - year
print("Sizning yoshingiz:", age, "\n")


# ================================
# 2. Extract Car Name ('LMaasleitbtui')
# Sharti: Matndan mashina nomi chiqaring.
# Oddiy qilib harflarni tanlaymiz → 'Lamb'
# ================================
txt1 = 'LMaasleitbtui'
car1 = txt1[0] + txt1[2] + txt1[4] + txt1[6] + txt1[8] + txt1[10] + txt1[12]
print(" Mashina nomi:", car1, "\n")


# ================================
# 3. Extract Car Name ('MsaatmiazD')
# Sharti: Matndan mashina nomi chiqaring.
# Bu yerda 'Mazda' harflarini olamiz.
# ================================
txt2 = 'MsaatmiazD'
car2 = txt2[0] + txt2[3] + txt2[4] + txt2[6] + txt2[8]
print(" Mashina nomi:", car2, "\n")


# ================================
# 4. Extract Residence Area
# Sharti: "I am from London" matnidan qayerdanligini oling.
# ================================
txt = "I'am John. I am from London"
words = txt.split()
area = words[-1]
print(" Yashash joyi:", area, "\n")


# ================================
# 5. Reverse String
# Sharti: Kiritilgan matnni teskari chiqarish
# ================================
s = input(" Matn kiriting (teskari bo'ladi): ")
print("Natija:", s[::-1], "\n")


# ================================
# 6. Count Vowels
# Sharti: Matndagi unli harflar sonini sanash
# ================================
s2 = input(" Unli sanash uchun matn: ")
vowels = "aeiouAEIOU"
count = 0
for ch in s2:
    if ch in vowels:
        count += 1
print("Unlilar soni:", count, "\n")


# ================================
# 7. Find Maximum Value
# Sharti: Listdagi eng katta sonni topish
# ================================
nums = [3, 8, 12, 5, 40, 7]
print(" Ruyxat:", nums)
print("Eng katta son:", max(nums), "\n")


# ================================
# 8. Check Palindrome
# Sharti: So'z palindrom ekanligini tekshirish
# ================================
word = input(" So'z kiriting: ")
if word == word[::-1]:
    print("Bu palindrom\n")
else:
    print("Palindrom emas\n")


# ================================
# 9. Extract Email Domain
# Sharti: Emaildan domain qismi ajratib olish
# ================================
email = input(" Email kiriting: ")
domain = email.split('@')[1]
print("Email domain:", domain, "\n")


# ================================
# 10. Generate Random Password
# Sharti: Tasodifiy parol yaratish
# ================================
import random
chars = "abc123!@#"
password = ""
for i in range(8):   # 8 belgili parol
    password += random.choice(chars)
print("10) Tasodifiy parol:", password)

