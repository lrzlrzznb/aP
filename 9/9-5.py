from collections import deque
def construct_graph(words):
    graph = {}
    for word in words:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i + 1:]
            if pattern not in graph:
                graph[pattern] = []
            graph[pattern].append(word)
    return graph
def bfs(start, end, graph):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        word, path = queue.popleft()
        if word == end:
            return path
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i + 1:]
            if pattern in graph:
                neighbors = graph[pattern]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))
    return None
def word_ladder(words, start, end):
    graph = construct_graph(words)
    return bfs(start, end, graph)
n = int(input())
words = [input().strip() for _ in range(n)]
start, end = input().strip().split()
result = word_ladder(words, start, end)
if result:
    print(' '.join(result))
else:
    print("NO")
