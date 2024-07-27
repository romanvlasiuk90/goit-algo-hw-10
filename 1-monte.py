import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Обчислення інтеграла методом Монте-Карло
def monte_carlo_integration(f, a, b, num_points=10000):
    points_under_curve = 0
    for _ in range(num_points):
        x = random.uniform(a, b)
        y = random.uniform(0, f(b))
        if y <= f(x):
            points_under_curve += 1
    area = (b - a) * f(b) * (points_under_curve / num_points)
    return area

# Використання методу Монте-Карло для обчислення інтеграла
mc_integral = monte_carlo_integration(f, a, b)
print("Інтеграл методом Монте-Карло:", mc_integral)

# Обчислення інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)
print("Інтеграл за допомогою функції quad:", result)

# Висновки у форматі markdown
markdown_output = f"""
# Висновки

## Результати обчислень

- **Інтеграл методом Монте-Карло**: {mc_integral}
- **Інтеграл за допомогою функції quad**: {result}

## Аналіз

Метод Монте-Карло показав наближений результат, який є близьким до аналітичного значення, отриманого за допомогою функції `quad` з бібліотеки `SciPy`. Цей метод є ефективним для обчислення інтегралів, коли аналітичне обчислення є складним або неможливим. Проте, точність методу Монте-Карло залежить від кількості точок вибірки: чим більше точок, тим точніший результат.

## Висновок

Для інтегралів, які можуть бути обчислені аналітично, функція `quad` є більш точним та надійним методом. Однак, метод Монте-Карло є гарним інструментом для наближеного обчислення інтегралів у складних випадках.
"""

# Збереження висновків у файл readme.md
with open('readme.md', 'w', encoding='utf-8') as f:
    f.write(markdown_output)