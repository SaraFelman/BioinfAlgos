#  2 Find the Length of a Longest Path in a Manhattan-like Grid
# Длина самого длинного пути в туристической задаче Манхэттена
# Найдите длину самого длинного пути в прямоугольном городе.

# Дано: целые числа n и m, за которыми следуют матрица n × ( m +1) Down и матрица ( n +1) × m Right
# Две матрицы разделены символом «-».
# Возврат: длина самого длинного пути от источника (0, 0) до приемника ( n , m ) в прямоугольной сетке
# размером n × m , края которой определяются матрицами Down и Right
# Образец набора данных
# 4 4
# 1 0 2 4 3
# 4 6 5 2 1
# 4 4 5 2 1
# 5 6 8 5 3
# -
# 3 2 4 0
# 3 2 4 2
# 0 7 3 3
# 3 3 0 2
# 1 3 2 2
# Пример вывода
# 34

#  2 Find the Length of a Longest Path in a Manhattan-like Grid
def manhattan_tourist(n, m, down, right):
    s = [[0] * (m + 1) for _ in range(n + 1)] # создаем таблицу размера где все элементы нули

    for i in range(1, n + 1): # заполняем первый столбец
        s[i][0] = s[i - 1][0] + down[i - 1][0] # путь до (i,0) = путь до (i-1,0) + вес ребра вниз

    for j in range(1, m + 1): # заполняем первую строку
        s[0][j] = s[0][j - 1] + right[0][j - 1] # путь до (0,j) = путь до (0,j-1) + вес ребра вправо

    for i in range(1, n + 1): # проходимся циклом по остальной части матрицы, идем по всем строкам кроме первой (i=0)
        for j in range(1, m + 1): # а тут по всем столбцам кроме первого (j=0), так как его уже тоже заполнили
            from_top = s[i - 1][j] + down[i - 1][j] # если пришли сверху
            # - s[i-1][j] - длина самого длинного пути до точки (i-1,j)
            # - down[i-1][j] - вес вертикального ребра из (i-1,j) в (i,j)
            # - from_top = путь сверху + вес движения вниз

            from_left = s[i][j - 1] + right[i][j - 1] # если пришли слева
            # - s[i][j-1] - длина самого длинного пути до точки (i,j-1)
            # - right[i][j-1] - вес горизонтального ребра из (i,j-1) в (i,j)
            # аналогично from_left = путь слева + вес движения вправо

            s[i][j] = max(from_top, from_left)
            # - Выбираем макс значение из from_top и from_left тк ищем самый длинный путь

    return s[n][m] # вернули результат

if __name__ == "__main__":
    n, m = map(int, input().split()) # считали размер сетки
    down_str = []
    right_str = []
    while True: # записали всё что до "-" в down_str = []
        a = input()
        if a == "-":
            break
        down_str.append(a)
    while True: # записали всё что до "" в right_str = []
        a = input()
        if a == "":
            break
        right_str.append(a)

    down = []
    for row in down_str: # здесь и ниже обрабатываем строки
        numbers = list(map(int, row.split()))
        # row.split() разбивает строку по пробелам
        # map(int, ...) преобразует каждый элемент в целое число
        # в конце делаем из этого список
        down.append(numbers)
        # вот так по итогу будет выглядеть ["1 0 2 4 3", "4 6 5 2 1", "4 4 5 2 1", "5 6 8 5 3"] вот так по итогу будет выглядеть

    right = []
    for row in right_str:
        numbers = list(map(int, row.split()))
        right.append(numbers)
    # print(down)
    # print(right)

    print(manhattan_tourist(n, m, down, right)) #выводим результат

# # Альтернативная версия с пошаговым выводом
# def manhattan_tourist_debug(n, m, down, right):
#     """Версия с отладочным выводом"""
#     s = [[0] * (m + 1) for _ in range(n + 1)]
#
#     print(f"\nИнициализация матрицы s размером {(n + 1)}x{(m + 1)}")
#     print(f"s[0][0] = 0")
#
#     # Заполнение первого столбца
#     print(f"\n1. Заполняем первый столбец (i от 1 до {n}):")
#     for i in range(1, n + 1):
#         s[i][0] = s[i - 1][0] + down[i - 1][0]
#         print(f"   s[{i}][0] = s[{i - 1}][0] + down[{i - 1}][0] = {s[i - 1][0]} + {down[i - 1][0]} = {s[i][0]}")
#
#     # Заполнение первой строки
#     print(f"\n2. Заполняем первую строку (j от 1 до {m}):")
#     for j in range(1, m + 1):
#         s[0][j] = s[0][j - 1] + right[0][j - 1]
#         print(f"   s[0][{j}] = s[0][{j - 1}] + right[0][{j - 1}] = {s[0][j - 1]} + {right[0][j - 1]} = {s[0][j]}")
#
#     # Заполнение остальной таблицы
#     print(f"\n3. Заполняем остальную таблицу:")
#     for i in range(1, n + 1):
#         print(f"   Строка {i}:")
#         for j in range(1, m + 1):
#             from_top = s[i - 1][j] + down[i - 1][j]
#             from_left = s[i][j - 1] + right[i][j - 1]
#             s[i][j] = max(from_top, from_left)
#             print(f"     s[{i}][{j}] = max(s[{i - 1}][{j}]+down[{i - 1}][{j}], s[{i}][{j - 1}]+right[{i}][{j - 1}])")
#             print(f"                = max({s[i - 1][j]}+{down[i - 1][j]}, {s[i][j - 1]}+{right[i][j - 1]})")
#             print(f"                = max({from_top}, {from_left}) = {s[i][j]}")
#
#     print(f"\n4. Результат: s[{n}][{m}] = {s[n][m]}")
#     return s[n][m]
#
#
# if __name__ == "__main__":
#     # Запуск теста
#     # print("Запускаем тест на примере...")
#     # if test_example():
#     #     print("Тест пройден успешно!")
#     # else:
#     #     print("Тест не пройден!")
#
#     # Запуск отладочной версии
#     print("Отладочная версия с пошаговым выводом:")
#     n = 4
#     m = 4
#     down = [
#         [1, 0, 2, 4, 3],
#         [4, 6, 5, 2, 1],
#         [4, 4, 5, 2, 1],
#         [5, 6, 8, 5, 3]
#     ]
#     right = [
#         [3, 2, 4, 0],
#         [3, 2, 4, 2],
#         [0, 7, 3, 3],
#         [3, 3, 0, 2],
#         [1, 3, 2, 2]
#     ]
#
#     result = manhattan_tourist_debug(n, m, down, right)
#     print(f"\nИтоговый результат: {result}")