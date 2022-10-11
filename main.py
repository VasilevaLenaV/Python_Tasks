# Задача 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def calculate_distance(x1, y1, x2, y2):
     return int((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)) * 100) / 100


X1, Y1, X2, Y2 = float(input("Задача 5. Введите x1 - ")), float(input("y1 - ")), float(input("x2 - ")), float(input("y2 - "))
print(f'Расстояние между точками {calculate_distance(X1, Y1, X2, Y2)}')
