# 3 Find the Longest Path in a DAG
# Самый длинный путь в задаче DAG
# Найдите самый длинный путь между двумя узлами в DAG с весовыми ребрами.

# Дано: целое число, представляющее исходный узел графа, за которым следует целое число,
# представляющее конечный узел графа, и далее граф с весами ребер. Граф представлен
# модифицированным списком смежности, в котором запись «0->1:7» означает, что ребро
# соединяет узел 0 с узлом 1 с весом 7.
# Возврат: длина самого длинного пути в графе, за которым следует самый длинный путь.
# (Если существует несколько самых длинных путей, можно вернуть любой из них.)
#
# Образец набора данных
# 0
# 4
# 0->1:7
# 0->2:4
# 2->3:2
# 1->4:1
# 3->4:3
# Пример вывода
# 9
# 0->2->3->4

from collections import defaultdict

def read_input():
    source = int(input().strip()) # вводим данные, преобразуем к инту, убираем по краям пробелы
    sink = int(input().strip())

    graph = defaultdict(list) # создаем словарь, где по умолчанию в значениях пустые списки
                                # чтобы не было ошибки при обращении к несуществующему ключу
    while True:
        try:
            line = input().strip() # чтение строки с ребром
            if not line:  # проверка на пустую строку
                break

            if '->' in line and ':' in line: # Проверка на то что у нас правильный формат строки
                parts = line.split('->') # Делим строку по '->' и получается ["0", "1:7"]
                from_node = int(parts[0]) # Обираем исходную вершину from_node = 0
                to_part = parts[1].split(':') # Делим строку по ':' и получается ["1", "7"]
                to_node = int(to_part[0]) # кладем целевую вершину
                weight = int(to_part[1]) # кладем вес ребра

                graph[from_node].append((to_node, weight)) # Добавили ребро в граф, теперь graph[0] = [(1, 7), (2, 4)]
        except EOFError: # Проверка на End Of File
            break

    return source, sink, graph  #source - исходная вершина, sink - конечная вершина, graph - граф

def topological_sort(graph):
    in_degree = defaultdict(int)     # in_degree[] будет хранить сколько ребер входит в вершину

    all_nodes = set() #set() создаем пустое множество
    for node in graph: # проходим по всем вершинам графа
        all_nodes.add(node) # добавляем текущую вершину в множество всех вершин
        for neighbor, _ in graph[node]: # идем по всем соседям текущей вершины, вес ребра нас не интересует поэтому _
            all_nodes.add(neighbor)  # добавляем соседа
            in_degree[neighbor] += 1 # и увеличиваем счетчик входящих ребер для соседа


    zero_in_degree = [node for node in all_nodes if in_degree[node] == 0] #находим вершины с нулевой степенью захода
    # Проходимся по всем вершинам в all_nodes и если in_degree[вершина] == 0, то добавляем вершину в список
    topo_order = []

    queue = zero_in_degree #  Используем список как очередь
    queue_index = 0 # queue_index указывает на текущий элемент в "очереди", задали начальное значение

    # пока индекс меньше длины очереди в очереди еще есть элементы для обработки
    while queue_index < len(queue):
        # берем вершину по индексу
        current = queue[queue_index]
        # увеличиваем индекс, чтобы в следующий раз взять следующий элемент
        queue_index += 1
        # добавляем текущую вершину в конец списка topo_order
        topo_order.append(current)

        # Проходим по всем ребрам, исходящим из current игнорируя вес ребра
        for neighbor, _ in graph[current]:
            in_degree[neighbor] -= 1 # как бы удаляем текущую вершину из графа
            if in_degree[neighbor] == 0: # если у neighbor больше нет входящих ребер значит все его предшественники уже обработаны
                queue.append(neighbor) # добавляем neighbor в конец списка queue

    return topo_order


def longest_path_no_deque(graph, source, sink):
    # Cоздаем множество, проходимся по графу добавляя текущую вершину в all_nodes и далее цикл по соседям текущей
    # и их добавление в all_nodes
    all_nodes = set()
    for node in graph:
        all_nodes.add(node)
        for neighbor, _ in graph[node]:
            all_nodes.add(neighbor)

    dist = {node: float('-inf') for node in all_nodes} # dist = {0: -∞, 1: итд
    dist[source] = 0 # расстояние от source до самого source = 0 и теперь dist = {0: 0, 1: -∞, 2: -∞, 3: -∞, 4: -∞}

    # сделали словарь предшественников, prev[вершина] будет хранить вершину, из которой мы пришли,
    # если не знаем откуда пришли будет None
    prev = {node: None for node in all_nodes}

    # Список вершин в топологическом порядке
    topo_order = topological_sort(graph)

    for node in topo_order:
        # Проверяем, можно ли добраться до вершины node из исходной вершины source
        if dist[node] != float('-inf'):   # dist[0] = 0 ≠ -∞ → True
            # Для каждой достижимой вершины рассматриваем все её соседей
            for neighbor, weight in graph[node]: # graph[0] = [(1,7), (2,4)]
                # Вычисляем длину пути до neighbor через текущую вершину node
                new_dist = dist[node] + weight  # new_dist = 0 + 7 = 7
                # Сравниваем новый путь с текущим лучшим путём до neighbor, нам нужен максимальный
                if new_dist > dist[neighbor]: # 7 >  dist[1] = -∞ -∞ → True
                    # Если нашли более длинный путь - обновляем:
                    dist[neighbor] = new_dist  # dist[1] = 7
                    prev[neighbor] = node # prev[1] = 0 (в вершину 1 пришли из 0)

    path = []
    current = sink # начинаем с конечной вершины
    while current is not None:
        path.append(current)   # пока current не None добавляем текущ вершину в путь
        current = prev[current] # Переход к предшественнику

    path.reverse() # разворот списка

    # - Проверяем: если not path: не нашли путь, если path[0] != source: путь не начинается с source
    if not path or path[0] != source:
        return float('-inf'), []

    return dist[sink], path

    # Преобразование пути в строку чтобы было как в условии
def format_path(path):
    return '->'.join(map(str, path))



if __name__ == "__main__": # вчитываем данные, приемняем функцию, принтим результат и путь если он существует
    source, sink, graph = read_input()

    max_length, path = longest_path_no_deque(graph, source, sink)

    print(int(max_length))
    if path:
        print(format_path(path))


# if __name__ == "__main__":
#     main()

# def longest_path(graph, source, sink):
#     for s_b in graph:
#         s_b = float("inf")
#     source = 0
