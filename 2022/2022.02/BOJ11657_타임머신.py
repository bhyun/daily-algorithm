import sys

def search(node):
    dist[node] = 0
    for i in range(n):
        for a, b, c in edges:
            if dist[a] != sys.maxsize and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                if i == n - 1:
                    return False
    return True

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
dist = [sys.maxsize] * (n+1)

if not search(1):
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == sys.maxsize:
            print(-1)
        else:
            print(dist[i])