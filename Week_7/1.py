# Вычислить сумму и количество элементов,
# находящихся под главной диагональю квадратной матрицы B(n, n),
# переписать эти элементы в одномерный массив P(n(n–1)/2).

import numpy as np

n = int(input())
a = (np.arange(1, n*n+1).reshape(n,n))
print(a)

h = []
summa = 0
kol_vo = 0

for i in range(n):
    for j in range(i):
        h.append(int(a[i][j]))
summa = sum(h)
kol_vo = len(h)

print(h)
print("Сумма:", summa)
print("Количество элементов:", kol_vo)
#     b = a.sum(axis=1)
# print(b)

# quant =
# for i in a:
#     if
#     a.sum(axis=0)
# print("Сумма по столбцам\n", po_osi.sum(axis=0),"\n")
# print()