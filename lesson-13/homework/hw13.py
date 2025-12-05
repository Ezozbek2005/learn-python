# 1-misol
from datetime import date

# Foydalanuvchidan tug‘ilgan sanani olish
y = int(input("Tug'ilgan yilingizni kiriting: "))
m = int(input("Tug'ilgan oyingizni kiriting (1-12): "))
d = int(input("Tug'ilgan kuningizni kiriting: "))

# Bugungi sana
today = date.today()

# Tug'ilgan sana
birth_date = date(y, m, d)

# Yoshni hisoblash
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

# Agar kun manfiy bo'lsa, oldingi oydan qarz olamiz
if days < 0:
    months -= 1
    # O'tgan oydagi kunlar sonini topish
    from calendar import monthrange
    prev_month = today.month - 1 if today.month > 1 else 12
    prev_year = today.year if today.month > 1 else today.year - 1
    days += monthrange(prev_year, prev_month)[1]

# Agar oy manfiy bo'lsa, yilni kamaytiramiz
if months < 0:
    years -= 1
    months += 12

# Natija
print(f"\nSizning yoshingiz: {years} yil, {months} oy, {days} kun.")

2-misol
from datetime import date

# Foydalanuvchidan tug'ilgan sana
y = int(input("Tug'ilgan yilingizni kiriting: "))
m = int(input("Tug'ilgan oyingizni kiriting (1-12): "))
d = int(input("Tug'ilgan kuningizni kiriting: "))

today = date.today()

# Joriy yil uchun tug'ilgan kun sanasi
next_birthday = date(today.year, m, d)

# Agar tug'ilgan kun o'tib ketgan bo'lsa — keyingi yilga o‘tamiz
if next_birthday < today:
    next_birthday = date(today.year + 1, m, d)

# Farqni hisoblash
days_left = (next_birthday - today).days

print(f"Keyingi tug'ilgan kuningizga {days_left} kun qoldi.")

# 3-misol
from datetime import datetime, timedelta

# 1️⃣ Foydalanuvchidan joriy sana va vaqtni olish
current_datetime_str = input("Joriy sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")

# 2️⃣ Foydalanuvchidan uchrashuv davomiyligini olish
hours = int(input("Uchrashuv davomiyligi soatlarda: "))
minutes = int(input("Uchrashuv davomiyligi minutlarda: "))

# 3️⃣ timedelta orqali davomiylikni hisoblash
meeting_duration = timedelta(hours=hours, minutes=minutes)

# 4️⃣ Uchrashuv tugash vaqtini hisoblash
end_datetime = current_datetime + meeting_duration

# 5️⃣ Natijani chiqarish
print("Uchrashuv tugaydi:", end_datetime.strftime("%Y-%m-%d %H:%M"))


4-misol
from datetime import datetime, timedelta

# 1️⃣ Foydalanuvchidan sana va vaqtni olish
dt_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

# 2️⃣ Foydalanuvchidan joriy va maqsad vaqt zonasi soat farqini olish
current_offset = int(input("Joriy vaqt zonasining UTC farqini kiriting (masalan +5): "))
target_offset = int(input("Maqsad vaqt zonasining UTC farqini kiriting (masalan 0): "))

# 3️⃣ Farqni hisoblash
offset_diff = target_offset - current_offset
dt_target = dt + timedelta(hours=offset_diff)

# 4️⃣ Natijani chiqarish
print("Vaqt maqsad vaqt zonasida:", dt_target.strftime("%Y-%m-%d %H:%M"))


5-misol

from datetime import datetime
import time

# 1️⃣ Foydalanuvchidan maqsad vaqtni olish
target_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

# 2️⃣ Taymer
while True:
    now = datetime.now()
    diff = target_time - now

    if diff.total_seconds() <= 0:
        print("\nVaqt tugadi!")
        break

    # Qolgan vaqtni kun-soat-daqiqa-soniya qilib ajratish
    days = diff.days
    seconds = diff.seconds

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    print(f"\rQolgan vaqt: {days} kun, {hours:02d}:{minutes:02d}:{seconds:02d}", end="")
    time.sleep(1)

6 - misol
email = input("Email kiriting: ")

if "@" in email and "." in email:
    at_index = email.index("@")
    dot_index = email.rindex(".")

    if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
        print("Email to'g'ri!")
    else:
        print("Email xato formatda!")
else:
    print("Email xato formatda!")

7-misol
phone = input("Telefon raqam kiriting (faqat raqamlar): ")

if len(phone) == 10 and phone.isdigit():
    part1 = phone[0:3]
    part2 = phone[3:6]
    part3 = phone[6:10]

    formatted = f"({part1}) {part2}-{part3}"
    print("Formatlangan raqam:", formatted)
else:
    print("Xato! 10 ta raqam kiriting!")

# 8 - misol
password = input("Parolni kiriting: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Parol kuchli!")
else:
    print("Parol kuchsiz!")


9-masala
text = "Bugun havo yaxshi. Bugun men maktabga bordim. Bugun dars bo'ldi."

word = input("Qaysi so'zni qidiramiz? ")

count = text.lower().count(word.lower())

print(f"So'z {count} marta uchradi.")


# 10 - masala
import re

text = input("Matn kiriting: ")

pattern = r"\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}\.\d{2}\.\d{4}"

dates = re.findall(pattern, text)

print("Topilgan sanalar:")
for d in dates:
    print(d)
