
#Завдання 1
n = 20
s = 0
k = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        s += i
        k += 1

print(k)
print(s)
if k > 0:
    print(round(s / k, 2))
#Завдання 2
n = 50742
t = n
k = 0
s = 0
mx = 0
mn = 9

if n == 0:
    k = 1
    mn = 0
else:
    while t > 0:
        d = t % 10
        k += 1
        s += d
        if d > mx:
            mx = d
        if d < mn:
            mn = d
        t //= 10

print(k)
print(s)
print(mx)
print(mn)
#Завдання 3
n = 30
for num in range(1, n + 1):
    t = num
    ok = True
    zero = False
    
    while t > 0:
        d = t % 10
        if d == 0:
            zero = True
            break
        if num % d != 0:
            ok = False
            break
        t //= 10
        
    if not zero and ok:
        print(num, end=" ")
#Завдання 4
w = 6
h = 4
b = "#"
a = "."
if w < 3 or h < 3:
    print("Помилка")
else:
    for r in range(h):
        for c in range(w):
            if r == 0 or r == h - 1 or c == 0 or c == w - 1:
                print(b, end="")
            else:
                print(a, end="")
        print()
#Додаткове завдання
h = 5
if h < 3:
    print("Помилка")
else:
    for r in range(1, h + 1):
        for c in range(r):
            print("*", end="")
        print()
