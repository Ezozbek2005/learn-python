# 1-misol
import threading

# Prime son tekshirish funksiyasi
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Thread uchun funksiyasi
def check_primes(numbers, result_list):
    for num in numbers:
        if is_prime(num):
            result_list.append(num)

# Asosiy dastur
numbers = list(range(1, 51))  # 1 dan 50 gacha
num_threads = 4
threads = []
results = []

# Sonlarni teng bo‘laklarga bo‘lish
step = len(numbers) // num_threads

for i in range(num_threads):
    start = i * step
    # Oxirgi thread oxirgi songacha oladi
    end = (i + 1) * step
    if i == num_threads - 1:
        end = len(numbers)
    
    t = threading.Thread(target=check_primes, args=(numbers[start:end], results))
    threads.append(t)
    t.start()

# Hamma thread tugashini kutish
for t in threads:
    t.join()

results.sort()
print("Tub sonlar:", results)

# 2- misol
import threading
from collections import defaultdict

# Thread uchun funksiyasi
def count_words(lines, result_dict):
    local_count = defaultdict(int)
    for line in lines:
        # Vergullarni bo‘sh joyga almashtirish
        line = line.replace(',', ' ')
        # Kichik harfga o‘tkazish va so‘zlarga ajratish
        words = line.strip().lower().split()
        for w in words:
            local_count[w] += 1
    # Natijalarni umumiy dict ga qo‘shish
    for w, c in local_count.items():
        result_dict[w] += c

# Asosiy dastur
filename =  "C:\\Users\\user\\Downloads\\Telegram Desktop\\emails (2).txt"
num_threads = 4
threads = []
final_counts = defaultdict(int)

# Faylni o‘qish
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Threadlar uchun satrlarni bo‘lish
step = len(lines) // num_threads
for i in range(num_threads):
    start = i * step
    end = (i + 1) * step if i != num_threads - 1 else len(lines)
    t = threading.Thread(target=count_words, args=(lines[start:end], final_counts))
    threads.append(t)
    t.start()

# Hamma thread tugashini kutish
for t in threads:
    t.join()

# Natijalarni chiqarish
for word, count in final_counts.items():
    print(f"{word}: {count}")
