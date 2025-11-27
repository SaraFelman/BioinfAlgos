# Даны числа L и t, строка Pattern образует ( L , t )-clump внутри
# (большей) строки Genome, если существует интервал Genome длиной L,
# в котором Pattern встречается не менее t раз.
# Например,ТГКА
# образует (25,3)-скопление в следующем геноме : gatcagcataagggtccc TGCA A TGCA TGACAAGCC TGCA gttgttttac
#
# Найдите паттерны, образующие clump в строке.
# Дано: строка Genome и целые числа k, L и t .
# Возврат: Все отдельные k-меры, образующие (L , t)-clump в геноме.

Genome = input()
k, L, t = map(int, input().split())

result_set = set()
result_list = []

for i in range(len(Genome) - L+1):
    window = Genome[i: i+L]
    # print(window, "window")

    kmer_count = {}
    for j in range(len(window) - k+1):
        kmer = window[j: j+k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1
        # print(kmer_count, "kmer")

    for kmer, count in kmer_count.items():
        if count >= t and kmer not in result_set:
            result_set.add(kmer)
            result_list.append(kmer)
# print(result_set)
print(result_list)
# CGACA GAAGA AATGT


#
Genome = input()
k, L, t = map(int, input().split())

result = set()

# Используем скользящее окно - обновляем только изменившиеся k-меры
window = Genome[:L]  # первое окно
kmer_count = {}

# Считаем k-меры для первого окна
for i in range(L - k + 1):
    kmer = window[i:i + k]
    kmer_count[kmer] = kmer_count.get(kmer, 0) + 1

# Проверяем первое окно
for kmer, count in kmer_count.items():
    if count >= t:
        result.add(kmer)

# Сдвигаем окно и обновляем счетчики
for i in range(1, len(Genome) - L + 1):
    # Удаляем k-mer, который выходит из окна
    old_kmer = Genome[i - 1:i - 1 + k]
    kmer_count[old_kmer] -= 1

    # Добавляем k-mer, который входит в окно
    new_kmer = Genome[i + L - k:i + L]
    kmer_count[new_kmer] = kmer_count.get(new_kmer, 0) + 1

    # Проверяем новый k-mer
    if kmer_count[new_kmer] >= t:
        result.add(new_kmer)

print(' '.join(sorted(result)))

# def find_clumps_with_sorting(genome, k, L, t):
#     result = set()
#     n = len(genome)
#
#     for start in range(n - L + 1):
#         window = genome[start:start + L]
#
#         # Генерируем все k-меры в окне
#         kmers = [window[i:i + k] for i in range(len(window) - k + 1)]
#
#         # Сортируем k-меры
#         kmers.sort()
#
#         # Подсчитываем частоты в отсортированном массиве
#         count = 1
#         for i in range(1, len(kmers)):
#             if kmers[i] == kmers[i - 1]:
#                 count += 1
#             else:
#                 if count >= t:
#                     result.add(kmers[i - 1])
#                 count = 1
#
#         # Не забываем проверить последний k-mer
#         if count >= t and kmers:
#             result.add(kmers[-1])
#
#     return sorted(result)
#
# result = find_clumps_with_sorting(Genome, k, L, t)
# print(' '.join(result))
