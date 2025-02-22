def is_bipartite_dfs(graph, node, colors=None, color=0):

    if node in colors:
        return colors[node] == color  # Проверяем, что вершина уже окрашена правильно    
    colors[node] = color  # Красим текущую вершину в текущий цвет
    
    for neighbor in graph[node]:
        # Рекурсивно проверяем соседей, окрашивая их в противоположный цвет
        if not is_bipartite_dfs(graph, neighbor, colors, 1 - color):
            return False
    
    return True

def check_bipartite(graph):
    colors = {}  # Словарь для хранения информации о цветах вершин
    for node in graph:
        if node not in colors:  # Проверяем каждую компоненту связности
            if not is_bipartite_dfs(graph, node, colors):
                return False  # Если хоть одна компонента не двудольная, возвращаем False
    return True

n = int(input('Введите число людей: '))
against = list(map(int, input('Введите пары несовметимости, каждое число через пробел: ').split()))
graph = {}

for i in range(0, len(against), 2):
    if against[i] not in graph:
        graph[against[i]] = [against[i + 1]]
    else:
        graph[against[i]].append(against[i + 1])
    if against[i + 1] not in graph:
        graph[against[i + 1]] = [against[i]]
    else:
        graph[against[i + 1]].append(against[i])

print("Граф двудольный" if check_bipartite(graph) else "Граф не двудольный")