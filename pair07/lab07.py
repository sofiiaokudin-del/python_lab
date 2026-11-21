#Завдання 1. Аналіз текстового файлу
with open("text.txt", "r", encoding="utf-8") as f:
    t = f.read()

l = t.splitlines()
w = t.split()
m = ""
n = 0

for i, s in enumerate(l, start=1):
    if len(s) > len(m):
        m = s
        n = i

print(f"Рядків: {len(l)}")
print(f"Слів: {len(w)}")
print(f"Символів: {len(t)}")
print(f"Найдовший рядок: №{n}, {len(m)} символів")
print(f"Текст: {m}")
#Завдання 2. Пошук фрагмента у файлі
q = input("Фрагмент: ").strip().lower()
c = False

with open("text.txt", "r", encoding="utf-8") as f:
    for i, s in enumerate(f, start=1):
        r = s.strip()
        if q in r.lower():
            print(f"{i}: {r}")
            c = True

if not c:
    print("Збігів не знайдено.")
#Завдання 3. Результати студентів
a = []
with open("students.txt", "r", encoding="utf-8") as f:
    for s in f:
        if s.strip():
            p, b = s.strip().split(";")
            b = int(b)
            if b > 80:
                a.append([p, b])

a.sort(key=lambda x: x[1], reverse=True)

with open("result.txt", "w", encoding="utf-8") as f:
    for p, b in a:
        print(f"{p};{b}", file=f)
#Завдання 4. CSV-подібний журнал оцінок
def g(u):
    d = {}
    with open(u, "r", encoding="utf-8") as f:
        for s in f:
            if s.strip():
                p, k, o = s.strip().split(";")
                if p not in d:
                    d[p] = []
                d[p].append(int(o))
    return d


def h(d):
    v = []
    for p, o in d.items():
        e = sum(o) / len(o)
        v.append([p, len(o), e])
    v.sort(key=lambda x: x[2], reverse=True)
    return v


def z(v, u):
    with open(u, "w", encoding="utf-8") as f:
        for p, k, e in v:
            print(f"{p} — оцінок: {k} — середній: {e:.2f}", file=f)
        if v:
            x = v[0][2]
            y = [p for p, k, e in v if round(e, 2) == round(x, 2)]
            print(f"Найкращий результат: {' та '.join(y)} — {x:.2f}", file=f)


d = g("grades.csv")
v = h(d)
z(v, "report.txt")
#Додаткове завдання
with open("text.txt", "r", encoding="utf-8") as f:
    t = f.read().lower()

p = ".,!?;:—–-\"'()[]{}«»…"
for c in p:
    t = t.replace(c, " ")

d = {}
for w in t.split():
    d[w] = d.get(w, 0) + 1

s = sorted(d.items(), key=lambda x: (-x[1], x[0]))[:10]

with open("word_frequency.txt", "w", encoding="utf-8") as f:
    for w, n in s:
        print(f"{w}: {n}", file=f)