# 3 Построить граф де Брейна для набора k-меров
# Для произвольного набора k-меров Patterns (где некоторые k -меры могут встречаться
# несколько раз), мы определяем CompositionGraph ( Patterns ) как граф с | Patterns |
# изолированными рёбрами. Каждое ребро помечено k -мером из Patterns, а начальные и
# конечные узлы ребра помечены префиксом и суффиксом k -мера, маркирующего это ребро.
# Затем мы определяем граф де Брейна Patterns , обозначаемый как DeBruijn ( Patterns ),
# путём склеивания одинаково помеченных узлов в CompositionGraph ( Patterns ),
# что приводит к следующему алгоритму.
#
# Дано: Коллекция узоров k-меров
# Возврат: Граф де Брейна ДеБрюйна (Patterns), в виде списка содержащего ребра графа

    # DeBruijn(Patterns): представьте  каждый k-мер в Patterns как изолированное ребро между
    # его префиксом и суффиксом,
    # склейте все узлы с одинаковыми метками, получая граф DeBruijn ( Patterns )
    # верните DeBruijn ( Patterns )

# Sample Dataset
# GAGG
# CAGG
# GGGG
# GGGA
# CAGG
# AGGG
# GGAG
# Sample Output
# AGG -> GGG
# CAG -> AGG,AGG
# GAG -> AGG
# GGA -> GAG
# GGG -> GGA,GGG

def DeBruijn(patterns: list[str]) -> dict[str, list[str]]:
    edges: dict[str, list[str]] = {}
    k = len(patterns[0])
    for kmer in patterns:
        if kmer[:k-1] in edges:
            edges[kmer[:k-1]].append(kmer[1:])
        else:
            edges[kmer[:k-1]] = [kmer[1:]]
    return edges


if __name__ == "__main__":
    patterns = []
    while True:
        a = input()
        if a == "":
            break
        patterns.append(a)

    # while s := input():
    #     patterns.append(s)

    dbrjn = DeBruijn(patterns)
    for key, value in dbrjn.items():
        print(key, "->", ",".join(value))
