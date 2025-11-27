# Определите "перекос" Genome строки ДНК, обозначенный Skew(Genome),
# как разницу между общим количеством вхождений «G» и «C» в геноме.
# Пусть Prefix i (Genome) обозначает префикс (т.е.начальную подстроку) генома длины i.
# Найдите положение в геноме, минимизирующее перекос.
# Дано: Геном строки ДНК.
# Возврат: все целые числа i, минимизирующие Skew(Prefixi (Text))
# по всем значениям i (от 0 до |Genome|).

#    C  A  T G G G C A T C G G C C A T A  C G  C  C
# 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

Genome = input()
values = [0]
count = 0
for i in Genome:
    if i == 'C':
        count = count - 1
        values.append(count)
    elif i == 'G':
        count = count + 1
        values.append(count)
    else:
        values.append(count)

mv = min(values)
for i, v in enumerate(values):
    if v == mv:
        print(i)