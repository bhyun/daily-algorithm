import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(node):
    for child, cost in tree[node]:
        if distance[child] == -1:
            distance[child] = distance[node] + cost
            dfs(child)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

distance = [-1] * (n+1)
distance[1] = 0
dfs(1)
x = distance.index(max(distance))

distance = [-1] * (n+1)
distance[x] = 0
dfs(x)
print(max(distance))