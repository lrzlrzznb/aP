from collections import defaultdict
def dfs(p):
    vis[p] = True
    for q in graph[p]:
        in_degree[q] -= 1
        if in_degree[q] == 0:
            dfs(q)
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    vis = [False] * (n + 1) 
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1
    for k in range(1, n + 1):  
        if in_degree[k] == 0 and not vis[k]:  
            dfs(k)
    flag = any(not vis[i] for i in range(1, n + 1))  
    print('Yes' if flag else 'No')
