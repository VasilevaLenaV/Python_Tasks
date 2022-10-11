# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


def is_weekend(dayweek):
    if 1 <= dayweek <= 5:
        print("нет")
    elif 6 <= dayweek <= 7:
        print("да")
    else:
        print("Введите день недели от 1 до 7")

day_of_week = int(input("Задача 1. Является ли день выходным. Введите день недели: "))
is_weekend(day_of_week)


# Задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def numbers_input(x):
    xyz = ["x", "y", "z"]
    a = []
    print("Задача 2. Истинность утверждения.")
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = numbers_input(3)

if check_predicate(statement) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")


# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def check_plane(x, y):
    if x > 0 and y > 0:
        print("1")
    elif x < 0 and y > 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    elif x > 0 and y < 0:
        print("4")
    else:
        print("Введите значение точек координат больше 0")

X = int(input("Задача 3. Введите кооринаты x: "))
Y = int(input("Введите кооринаты y: "))
check_plane(X, Y)


# Задача 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

def coordinate_plane(plane_input):
    if plane_input == 1:
        print("Диапазон точек в 1 плоскости: x > 0 и y > 0 ")
    elif plane_input == 2:
        print("Диапазон точек во 2 плоскости: x < 0 и y > 0 ")
    elif plane_input == 3:
        print("Диапазон точек в 3 плоскости: x < 0 и y < 0 ")
    elif plane_input == 4:
        print("Диапазон точек в 4 плоскости: x > 0 и y < 0 ")
    else:
        print("Введите номер четверти в рамках двухмерной системы координат")

plane = int(input("Задача 4. Введите номер плоскости: "))
coordinate_plane(plane)


# Задача 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def calculate_distance(x1, y1, x2, y2):
     return int((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)) * 100) / 100


X1, Y1, X2, Y2 = float(input("Задача 5. Введите x1 - ")), float(input("y1 - ")), float(input("x2 - ")), float(input("y2 - "))
print(f'Расстояние между точками {calculate_distance(X1, Y1, X2, Y2)}')
