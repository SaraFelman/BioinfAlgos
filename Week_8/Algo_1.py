# https://rosalind.info/problems/ba1i/
# Проблема часто встречающихся слов с несоответствиями
# Найдите наиболее частые k-меры с несовпадениями в строке.
# Дано: строка Text, а также целые числа k и d
# Возврат: все наиболее частые k- меры с несовпадениями до d в Тексте

# ф-я хемиша ищет кол-во отклонений между 2мя кмерами
# проходимся по строке, кмер в словарь с счетчиком  0
# тк 0 соседей у которых отклонение меньше чем задано
# следующий кмер сравнить со всем  что было до, если не совпад = 0
# потом следующий, если есть сосед у которого меньше откл чем задано,
# то добавим им обоим по 1

text = input()
k, d = map(int, input().split())

def hamming(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Строки должны иметь одинаковую длину")
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance


def neighbour(pattern, mismatch, words):
    bases = ['A', 'T', 'G', 'C']
    for i in range(len(pattern)):
        for j in range(len(bases)):
            new_pattern = pattern[:i] + bases[j] + pattern[i + 1:]
            if mismatch <= 1:
                words.add(new_pattern)
            else:
                neighbour(new_pattern, mismatch - 1, words)

counts = {}
for i in range(len(text) - k + 1):
    kmer = text[i:i + k]

    neighbors = set()
    neighbour(kmer, d, neighbors)

    for neighbor in neighbors:
        counts[neighbor] = counts.get(neighbor, 0) + 1

# Находим максимальное значение счетчика
max_count = max(counts.values()) if counts else 0

# Собираем все k-меры с максимальным счетчиком
result_kmers = [kmer for kmer, count in counts.items() if count == max_count]

# Сортируем результат для согласованности вывода
result_kmers.sort()
print(' '.join(result_kmers))

# # old code
# def hamming(s1, s2):
#     if len(s1) != len(s2):
#         raise ValueError("Строки должны иметь одинаковую длину")
#     distance = 0
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             distance += 1
#     return distance
# # print(hamming("1011101", "1001001"))
#
# def generate_all_kmers(k):
#     bases = ['A', 'C', 'G', 'T']
#     kmers = bases
#     for _ in range(k-1):
#         kmers = [kmer + base for kmer in kmers for base in bases]
#     return kmers
#
# kmer_count = {}
# for i in range(len(text) - k+1):
#     kmer = text[i: i+k]
#     if kmer not in kmer_count:
#         kmer_count[kmer] = 0
#
#     elif kmer in kmer_count:
#
# print(kmer_count)
# print(max(kmer_count, key=kmer_count.get))
#
# mismatch =
# if mismatch <= d:
#     kmer_count[kmer] += 1
