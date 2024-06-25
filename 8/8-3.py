class Node():
    def __init__(self, value, weight, visit):
        self.value = value
        self.weight = weight
        self.children = []
        self.visit = visit
        
def dfs(node):
    source = [node]
    answer = 0
    while source:
        subject = source.pop()
        if not subject.visit:
            subject.visit = True
            answer += subject.weight
            source += subject.children[::-1]
    return answer

n, m = map(int, input().split())
node_list = [Node(i, 0, False) for i in range(n)]
weight_list = list(map(int, input().split()))

for i in range(n):
    node_list[i].weight = weight_list[i]

for _ in range(m):
    a, b = map(int, input().split())
    node_list[a].children += node_list[b],
    node_list[b].children += node_list[a],

max_mass = 0
for node in node_list:
    if not node.visit:
        max_mass = max(max_mass, dfs(node))

print(max_mass)