import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(node):
    for neigh, dist in graph[node]:
        if distance[neigh] == -1:
            distance[neigh] = distance[node] + dist
            dfs(neigh)

v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    data = list(map(int, input().split()))
    cur, info = data[0], data[1:-1]
    for i in range(0, len(info)-1, 2):
        graph[cur].append((info[i], info[i+1]))

distance = [-1] * (v+1)
distance[1] = 0
dfs(1)
x = distance.index(max(distance))

distance = [-1] * (v+1)
distance[x] = 0
dfs(x)
print(max(distance))