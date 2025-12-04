# 2 Построить граф де Брюйна строки
# Для генома Text, PathGraph k (Text) представляет собой путь, состоящий из
# | Text | - k + 1 ребер, где i -е ребро этого пути помечено
# i-м k -мером в Text, а i-й узел пути помечен i -м ( k - 1) -мером в Text
# Граф де Брейна DeBruijn k ( Text ) образован путем склеивания одинаково
# помеченных узлов в PathGraph k ( Text ).
# Построить граф де Брейна строки.

# Дано: целое число k и строка Текст .
# Возврат: DeBruijn k ( Текст ), в виде списка смежности .
# Sample Dataset
# 4
# AAGATTCTCTAC
# Sample Output
# AAG -> AGA
# AGA -> GAT
# ATT -> TTC
# CTA -> TAC
# CTC -> TCT
# GAT -> ATT
# TCT -> CTA,CTC
# TTC -> TCT

from ba3e import DeBruijn


if __name__ == "__main__":
    k = int(input())
    text = input()

    patterns = []
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        patterns.append(kmer)

    dbrjn = DeBruijn(patterns)
    for key, value in dbrjn.items():
        print(key, "->", ",".join(value))
