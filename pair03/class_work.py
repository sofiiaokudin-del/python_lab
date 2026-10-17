"""
#Приклад 1. Перший і останній символ
text = input(&quot;Введіть слово: &quot;)
print(&quot;Перший:&quot;, text[0])
print(&quot;Останній:&quot;, text[-1])

#Приклад 2. Зрізи рядка
text = &quot;Programming&quot;
print(text[:7])
print(text[3:8])
print(text[::2])

#Приклад 3. Розворот рядка
text = input(&quot;Текст: &quot;)
print(text[::-1])

#Приклад 4. Підрахунок голосних, цифр і пробілів
text = input(&quot;Введіть текст: &quot;)
vowels = &quot;аеєиіїоуюяaeiou&quot;
vowel_count = 0
digit_count = 0
space_count = 0
for char in text.lower():
if char in vowels:
vowel_count += 1
if char.isdigit():
digit_count += 1
if char == &quot; &quot;:
space_count += 1
print(&quot;Голосних:&quot;, vowel_count)
print(&quot;Цифр:&quot;, digit_count)
print(&quot;Пробілів:&quot;, space_count)

#Приклад 5. Перевірка паліндрома після нормалізації
text = input(&quot;Текст: &quot;)
normalized = text.lower().replace(&quot; &quot;, &quot;&quot;)
if normalized == normalized[::-1]:
print(&quot;Паліндром&quot;)
else:
print(&quot;Не паліндром&quot;)

#Приклад 6. split() та join()
sentence = input(&quot;Речення: &quot;)
words = sentence.split()
print(words)
print(&quot;-&quot;.join(words))

#Приклад 7. Пошук найдовшого слова
sentence = input(&quot;Речення: &quot;)
words = sentence.split()
longest = words[0]
for word in words:
if len(word) &gt; len(longest):
longest = word
print(&quot;Найдовше слово:&quot;, longest)

#Приклад 8. replace() та очищення тексту
text = &quot; Python, Python, Python! &quot;
text = text.strip()
text = text.replace(&quot;Python&quot;, &quot;JavaScript&quot;)
print(text)

#Приклад 9. Перевірка простого ідентифікатора
code = input(&quot;Код: &quot;)
if code.isalnum() and code[0].isalpha():
print(&quot;Формат коректний&quot;)
else:
print(&quot;Некоректний формат&quot;)

#Приклад 10. Анаграми
text1 = input(&quot;Перший рядок: &quot;)
text2 = input(&quot;Другий рядок: &quot;)
a = text1.lower().replace(&quot; &quot;, &quot;&quot;)
b = text2.lower().replace(&quot; &quot;, &quot;&quot;)
if sorted(a) == sorted(b):
print(&quot;Анаграми&quot;)
else:
print(&quot;Не анаграми&quot;)

#Приклад 11. Простий зсув символів
text = input(&quot;Текст: &quot;)
result = &quot;&quot;
for char in text:
result += chr(ord(char) + 1)
print(&quot;Результат:&quot;, result)
"""