## 1-kvadrat   perimetri va yuzi
a = float(input("Kvadrat tomoni: "))
P = 4 * a
S = a * a
print("Perimetri:", P)
print("Yuzi:", S)

## 2- aylana deametri orqali yuzini topish
import math

d = float(input("Diametr: "))
L = math.pi * d
print("Aylana uzunligi:", L)

## 3-Ikki son a va b berilgan. O‘rtacha qiymat
a = float(input("a: "))
b = float(input("b: "))
c = (a + b) / 2
print("O'rtacha qiymat:", c)


## 4- Ikki son a va b. Ularning yig‘indisi, ko‘paytmasi va har birining kvadrati.
a = float(input("a: "))
b = float(input("b: "))

yigindi = a + b
kopaytma = a * b
kvadrat_a = a ** 2
kvadrat_b = b ** 2

print("Yig'indi:", yigindi)
print("Ko'paytma:", kopaytma)
print("a ning kvadrati:", kvadrat_a)
print("b ning kvadrati:", kvadrat_b)
