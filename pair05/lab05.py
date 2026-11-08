#Завдання 1. Площі геометричних фігур
def a(r):
  return 3.14159 * r**2
def b(w, h):
  return w * h

def c(x, y):
  return 0.5 * x * y

def main():
  s = input("Фігура: ").strip().lower()
  if s == "круг":
    r = float(input("Радіус: "))
    z = a(r)
    print(z)
  elif s == "прямокутник":
    w = float(input("Ширина: "))
    h = float(input("Висота: "))
    z = b(w, h)
    print(z)
  elif s == "трикутник":
    bx = float(input("Основа: "))
    hy = float(input("Висота: "))
    z = c(bx, hy)
    print(z)
main()

#Завдання 2. Функції для аналізу числа
def d(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True
def e(n):
  l = []
  for i in range(1, n + 1):
    if n % i == 0:
      l.append(i)
  return l
def f(n):
  s = 0
  for x in str(abs(n)):
    s += int(x)
  return s
def main():
  n = int(input("N = "))
  p = d(n)
  v = e(n)
  s = f(n)
  print(f"Просте число: {'так' if p else 'ні'}")
  print(f"Дільники: {v}")
  print(f"Сума цифр: {s}")
if __name__ == "__main__":
  main()

#Завдання 3. Звіт за списком оцінок
def a(g):
  return sum(g) / len(g)


def b(g):
  return min(g)


def c(g):
  return max(g)


def d(g, v):
  cnt = 0
  for x in g:
    if x > v:
      cnt += 1
  return cnt


def main():
  lst = [10, 8, 12, 9, 11]
  val = 9
  r1 = a(lst)
  r2 = b(lst)
  r3 = c(lst)
  r4 = d(lst, val)
  print(r1)
  print(r2)
  print(r3)
  print(r4)


if __name__ == "__main__":
  main()
#Завдання 4. Перевірка надійності пароля
def a(p):
  return len(p) >= 8
def b(p):
  for x in p:
    if x.isdigit():
      return True
  return False
def c(p):
  for x in p:
    if x.isupper():
      return True
  return False
def d(p):
  for x in p:
    if x.islower():
      return True
  return False
def e(p):
  for x in p:
    if not x.isalnum():
      return True
  return False

def validate_password(p):
  err = []
  if not a(p):
    err.append("мінімальна довжина менше 8 символів")
  if not b(p):
    err.append("немає цифри")
  if not c(p):
    err.append("немає великої літери")
  if not d(p):
    err.append("немає малої літери")
  if not e(p):
    err.append("немає спеціального символу")
  return len(err) == 0, err
pwd = input("Password: ")
ok, err = validate_password(pwd)
if ok:
  print("Пароль надійний.")
else:
  print("Пароль не відповідає вимогам.")
  print("Не виконано:", ", ".join(err))