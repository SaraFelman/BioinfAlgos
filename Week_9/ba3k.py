# 5
# К счастью, мы можем вывести контиги из графа де Брейна.
# Путь в графе называется неветвящимся, если in ( v ) = out ( v ) = 1
# для каждого промежуточного узла v этого пути, т.е. для каждого узла, за исключением,
# возможно, начального и конечного узлов пути. Максимальный неветвящийся путь —
# это неветвящийся путь, который нельзя продолжить в более длинный неветвящийся путь.
# Мы интересуемся этими путями, поскольку строки нуклеотидов, которые они записывают,
# должны присутствовать в любой сборке с заданным составом k -меров.
# По этой причине контиги соответствуют строкам, задаваемым максимальными неветвящимися
# путями в графе де Брейна.
#
# Проблема генерации контигов
# Сгенерировать контиги из коллекции прочтений (с несовершенным покрытием)
#
# Дано: Коллекция узоров k-меров
# Возврат: все контиги в DeBruijn(Patterns) в любом порядке


from collections import defaultdict

def DeBruijn(patterns: list[str]) -> dict[str, list[str]]:
    edges: dict[str, list[str]] = {}
    k = len(patterns[0])
    for kmer in patterns:
        if kmer[:k-1] in edges:
            edges[kmer[:k-1]].append(kmer[1:])
        else:
            edges[kmer[:k-1]] = [kmer[1:]]
    return edges


def calculate_degrees(edges):
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    print(out_degree)


    all_nodes = set() #удалили дубликаты сетом
    for node, neighbors in edges.items():
        all_nodes.add(node)
        all_nodes.update(neighbors)

    for node, neighbors in edges.items():
        out_degree[node] = len(neighbors)
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    for node in all_nodes:
        if node not in in_degree:
            in_degree[node] = 0
        if node not in out_degree:
            out_degree[node] = 0
        # print("in_degree",in_degree, "out_degree", out_degree, "all_nodes", all_nodes)

    return in_degree, out_degree, all_nodes


def is_1_in_1_out(node, in_degree, out_degree):
    return in_degree[node] == 1 and out_degree[node] == 1


def find_isolated_cycles(edges, in_degree, out_degree, nodes):
    visited = set()
    cycles = []

    for node in nodes:
        if is_1_in_1_out(node, in_degree, out_degree) and node not in visited:
            current = node #текущ вершины обхода
            cycle = []

            while is_1_in_1_out(current, in_degree, out_degree) and current not in visited:
                visited.add(current)
                cycle.append(current)
                if edges[current]:  # должен быть ровно 1 сосед!!
                    current = edges[current][0] # перешли к следующей вершинке
                else:
                    break

            # проверяем что в начале, это действительно цикл
            if len(cycle) > 1 and cycle[0] in edges[cycle[-1]]:
                # cycle[0] in edges[cycle[-1]] = 'A' in edges['C'] = 'A' in ['A'] = True
                cycle.append(cycle[0])  # замыкаем
                cycles.append(cycle)
            elif len(cycle) > 0:
                for v in cycle:
                    visited.add(v)

    return cycles


def maximal_non_branching_paths(edges, in_degree, out_degree, nodes):
    paths = []
    # u-v входящее ребро v узел v-w исходящ ребро х новый узел
    for v in nodes:
        if not is_1_in_1_out(v, in_degree, out_degree):
            if out_degree[v] > 0:
                for w in edges[v]:

                    non_branching_path = [v, w]

                    while is_1_in_1_out(w, in_degree, out_degree):
                        if edges[w]:          # всегда должен быть ровно один сосед
                            u = edges[w][0]
                            non_branching_path.append(u)
                            w = u
                        else:
                            break

                    paths.append(non_branching_path)

    isolated_cycles = find_isolated_cycles(edges, in_degree, out_degree, nodes)
    paths.extend(isolated_cycles)

    return paths


def paths_to_contigs(paths, k):
    contigs = []
    for path in paths:
        if len(path) == 0:
            continue

        contig = path[0]
        for i in range(1, len(path)):
            contig += path[i][-1]

        contigs.append(contig)

    return contigs


if __name__ == "__main__":
    patterns = []
    while True:
        a = input().strip()
        if a == "":
            break
        patterns.append(a)

    k = len(patterns[0])

    edges = DeBruijn(patterns)
    # print("edges", edges)

    in_degree, out_degree, nodes = calculate_degrees(edges)
    # print("in_degree", in_degree, "out_degree", out_degree, "nodes", nodes)

    paths = maximal_non_branching_paths(edges, in_degree, out_degree, nodes)
    # print("paths", paths)

    contigs = paths_to_contigs(paths, k)

    print(" ".join(sorted(contigs)))

