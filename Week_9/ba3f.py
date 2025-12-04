# 4 Эйлеров цикл
from copy import deepcopy
# Цикл, проходящий через каждое ребро графа ровно один раз,
# называется эйлеровым циклом , а граф, содержащий такой цикл, — эйлеровым
# Следующий алгоритм строит эйлеров цикл в произвольном ориентированном графе .
# Дано: Эйлеров ориентированный граф в форме списка смежности
# Возврат: Эйлеров цикл в этом графе.
# Образец набора данных
# 0 -> 3
# 1 -> 0
# 2 -> 1,6
# 3 -> 2
# 4 -> 2
# 5 -> 4
# 6 -> 5,8
# 7 -> 9
# 8 -> 7
# 9 -> 6
# Пример вывода
# 6->8->7->9->6->5->4->2->1->0->3->2->6

def find_cycle(graph: dict[str, list[str]], key: str) -> list[str]:
    cycle: list[str] = [key]
    while graph[key]:
        key = graph[key].pop(0) # вытащили значение из графа и теперь это кей
        cycle.append(key)
    for k in list(graph.keys()):
        if len(graph[k]) == 0:
            del graph[k]   # удаляем все ключи из которых повытаскали значение
    return cycle

def eulerian_cycle(graph: dict[str, list[str]]) -> list[str]:
    graph_copy = deepcopy(graph)
    cycle = find_cycle(graph_copy, list(graph_copy.keys())[0])
    while graph_copy:
        for new_start in cycle:
            if new_start in graph_copy:
                break

        new_cycle = find_cycle(graph_copy, new_start)
        for i in range(len(cycle)):
            if cycle[i] == new_start:
                cycle = cycle[:i] + new_cycle + cycle[i+1:]
                break
        # print(new_cycle)
    return cycle

  # form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
  #       while there are unexplored edges in Graph
  #           select a node newStart in Cycle with still unexplored edges
  #           form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
  #           Cycle ← Cycle’
  #       return Cycle


if __name__ == "__main__":
    v = 0
    patterns: dict[str, list[str]] = {}
    while True:
        a = input()
        if not a:
            break
        a = a.split(" -> ")
        patterns[a[0]] = a[1].split(",")
        v += len(patterns[a[0]])

    print(*eulerian_cycle(patterns), sep="->")
    # print(v)
    # print(len(patterns))
    # print(len(eulerian_cycle(patterns)))


