#Завдання 1. Аналіз і фільтрація списку
l = [12, 3, 4, 14, -12, 5, 10, 16, -4]

p = []
m = []
e = []
d = []

for x in l:
    if x > 0:
        p.append(x)
    if x < 0:
        m.append(x)
    if x % 2 == 0:
        e.append(x)
    if x % 3 == 0:
        d.append(x)

mi = min(l)
ma = max(l)
su = sum(l)
av = su / len(l)

print("Додатні:", p)
print("Від’ємні:", m)
print("Парні:", e)
print("Кратні 3:", d)
print(f"Min: {mi}; Max: {ma}; Sum: {su}; Average: {round(av, 2)}")

#Завдання 2. Дві групи учасників
g1 = {'Anna', 'Ivan', 'Olha'}
g2 = {'Ivan', 'Maksym', 'Olha'}

c_m = g1 & g2
o1 = g1 - g2
o2 = g2 - g1
al = g1 | g2

print("Спільні:", ", ".join(c_m))
print("Тільки group1:", ", ".join(o1))
print("Тільки group2:", ", ".join(o2))
print("Усі:", ", ".join(al))

#Завдання 3. Каталог товарів
ct = {
    "bread": 35,
    "milk": 48,
    "cheese": 120,
    "tea": 75
}

ct["bread"] = 38
ct["butter"] = 65

sr = "milk"
fd = ct.get(sr, "Товар не знайдено")
print(f"Пошук товару '{sr}': {fd} грн")

print("Товари в діапазоні 40..100 грн:")
for k, v in ct.items():
    if 40 <= v <= 100:
        print(f"{k} — {v} грн")

#Завдання 4. Журнал групив
gi = ('10-IT', '2026/2027')

st = {
    "Anna": [10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9]
}

nn = "Olha"
ng = [11, 12, 12, 10, 11]

if len(ng) == 5 and all(1 <= gr <= 12 for gr in ng):
    st[nn] = ng

print(f"{gi[0]} — {gi[1]}")

bs = ""
ha = 0

for n, gs in st.items():
    ag = sum(gs) / len(gs)
    print(f"{n} — {round(ag, 1)}")
    
    if ag > ha:
        ha = ag
        bs = n

print(f"Найкращий результат: {bs} — {round(ha, 1)}")
