import random
import statistics

def generate_grades(count):
    g = []
    for i in range(count):
        g.append(random.randint(1, 12))
    return g
def average_grade(grades):
    return round(statistics.mean(grades), 2)
def get_level(average):
    if average >= 10:
        return "високий"
    if average >= 7:
        return "достатній"
    if average >= 4:
        return "середній"
    return "початковий"

if __name__ == "__main__":
    t = generate_grades(5)
    a = average_grade(t)
    print(t, a, get_level(a))