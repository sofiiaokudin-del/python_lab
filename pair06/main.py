import tkinter as tk
import student_utils
def make_report():
    v = e.get().strip()

    if not v.isdecimal():
        t.delete("1.0", tk.END)
        t.insert(tk.END, "Помилка: введіть ціле число від 1 до 20.")
        return

    c = int(v)
    if c < 1 or c > 20:
        t.delete("1.0", tk.END)
        t.insert(tk.END, "Помилка: кількість оцінок має бути від 1 до 20.")
        return

    s = ["Anna", "Ivan", "Olha"]
    r = ""

    for n in s:
        g = student_utils.generate_grades(c)
        a = student_utils.average_grade(g)
        l = student_utils.get_level(a)
        r += f"{n}: {g} → {a} → {l}\n"

    print(r.strip())

    t.delete("1.0", tk.END)
    t.insert(tk.END, r)
w = tk.Tk()
w.title("Статистика учнів")
w.geometry("520x350")
tk.Label(w, text="Кількість оцінок (1–20):").pack(pady=5)
e = tk.Entry(w, width=20)
e.pack(pady=5)
tk.Button(w, text="Сформувати звіт", command=make_report).pack(pady=10)
t = tk.Text(w, width=60, height=12)
t.pack(pady=10)
w.mainloop()