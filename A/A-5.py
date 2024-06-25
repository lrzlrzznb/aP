def bfs(x, y):
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    queue = [(x, y)]
    distances = {(x, y): 0}
    while queue:
        current_x, current_y = queue.pop(0)
        for dx, dy in directions:
            new_x, new_y = current_x + dx, current_y + dy
            if 0 <= new_x < m and 0 <= new_y < n:
                if d[new_x][new_y] != '#':
                    new_distance = distances[(current_x, current_y)] + abs(int(d[new_x][new_y]) - int(d[current_x][current_y]))
                    if (new_x, new_y) not in distances or new_distance < distances[(new_x, new_y)]:
                        distances[(new_x, new_y)] = new_distance
                        queue.append((new_x, new_y))
    return distances
m, n, p = map(int, input().split())
d = []
for _ in range(m):
    row = input().split()
    d.append(row)
for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    if d[x1][y1] == '#' or d[x2][y2] == '#':
        print('NO')
        continue
    distances = bfs(x1, y1)
    if (x2, y2) in distances:
        print(distances[(x2, y2)])
    else:
        print('NO')