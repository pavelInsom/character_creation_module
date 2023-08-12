"""Добро пожаловать в самую лучшую программу
для вычисления квадратного корня из заданного числа.
"""

from math import sqrt


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return
    root = CalculateSquareRoot(your_number)
    print(f"""Мы вычислили квадратный корень из введённого вами числа.
          Это будет: {root}""")


print(__doc__)
calc(25.5)
