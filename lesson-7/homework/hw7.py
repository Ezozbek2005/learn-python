#1-masala: is_prime(n)

#Vazifa: Son tub bo‘lsa → True, bo‘lmasa → False.

def is_prime(n):
    # 2 dan kichik sonlar tub emas (0, 1)
    if n < 2:
        return False

    # 2 tub son
    if n == 2:
        return True

    # 2 dan katta juft sonlar tub emas
    if n % 2 == 0:
        return False

    # Faqat toq bo'luvchilarni tekshiramiz
    # √n gacha tekshirish kifoya
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # faqat toq sonlar
    return True

# 2-masala: digit_sum(k)

#Vazifa: Sonning raqamlari yig‘indisini qaytaradi.

def digit_sum(k):
    s = 0
    for digit in str(abs(k)):  # manfiy bo'lsa ham ishlasin
        s += int(digit)
    return s

# 3-masala: N dan oshmaydigan 2 ning darajalari

#Vazifa: 2, 4, 8, 16 ... ko‘rinishidagi barcha 2 ning darajalarini chop etadi.

def print_powers_of_two(N):
    p = 2
    while p <= N:
        print(p, end=" ")
        p *= 2

print(is_prime(7))     # True
print(is_prime(4))     # False

print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

print_powers_of_two(10)  # 2 4 8
