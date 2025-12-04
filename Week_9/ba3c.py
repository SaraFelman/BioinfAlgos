# 1 Постройте граф перекрытия набора k-меров
# В этой главе мы используем термины префикс и суффикс для обозначения первых
# k − 1 нуклеотидов и последних k − 1 нуклеотидов k -мера соответственно
# Для произвольного набора k-меров Patterns мы формируем граф
# содержащий узел для каждого k -мера из Patterns , и соединяем k- меры Pattern и Pattern"
# направленным ребром, если Suffix ( Pattern ) равен Prefix (Pattern')
# Полученный граф называется графом перекрытия этих k-меров и обозначается
# как Overlap (Pattern)
#
# Проблема перекрытия графов
# Построить граф перекрытия набора k-меров
#
# Дано: Коллекция паттернов k-меров
# Возврат: Граф перекрытия Overlap (Patterns), в виде списка смежности

# def Overlap(patterns: list[str]) -> dict[str, list[str]]:
#patterns = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]

# Sample Dataset
# ATGCG
# GCATG
# CATGC
# AGGCA
# GGCAT
# Sample Output
# AGGCA -> GGCAT
# CATGC -> ATGCG
# GCATG -> CATGC
# GGCAT -> GCATG

patterns = []
while True:
    a = input().strip() # чтобы было без пробелов с обоих сторон
    if a == "":
        break
    patterns.append(a)

k = len(patterns[0])
graph: dict[str, list[str]] = {}

for i in range(len(patterns)):
    for j in range(len(patterns)):
        if i != j:
            start = patterns[i]
            end = patterns[j]
            print(start, end)
            if start[1:] == end[:k-1]:
                graph[start] = [end]

for key, value in graph.items():
    print(key, "->", ",".join(value))

# if __name__ == "__main__":
#     patterns = []
#     while True:
#         a = input()
#         if a == "":
#             break
#         patterns.append(a)
#
#     dbrjn = DeBruijn(patterns)
#     for key, value in dbrjn.items():
#         print(key, "->", ",".join(value))