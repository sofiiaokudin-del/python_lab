#Завдання 1. Геометричні обчислення з math 
import math

r = float(input("Радіус: "))
a = float(input("Перший катет: "))
b = float(input("Другий катет: "))
n = int(input("Предметів: "))
k = int(input("В упаковці: "))

s = round(math.pi * r ** 2, 2)
c = round(math.sqrt(a ** 2 + b ** 2), 2)
p = math.ceil(n / k)
print("Площа круга:", s)
print("Гіпотенуза:", c)
print("Потрібно упаковок:", p)
#Завдання 2. Генератор оцінок і статистичний звіт
import random
import statistics

n = int(input("N: "))
if n <= 0:
    print("N повинно бути додатним")
else:
    g = []
    for i in range(n):
        g.append(random.randint(1, 12))

    c = 0
    for x in g:
        if x >= 10:
            c += 1
    print("Оцінки:", g)
    print("Min:", min(g))
    print("Max:", max(g))
    print("Середнє:", round(statistics.mean(g), 2))
    print("Медіана:", statistics.median(g))
    print("Оцінок 10–12:", c)
#Завдання 3. Дата події
from datetime import date

s = input("Дата події (РРРР-ММ-ДД): ")
y, m, d = map(int, s.split("-"))
e = date(y, m, d)
t = date.today()
r = (e - t).days

if r > 0:
    print("До події залишилося:", r, "днів")
elif r < 0:
    print("Після події минуло:", abs(r), "днів")
else:
    print("Подія сьогодні!")

