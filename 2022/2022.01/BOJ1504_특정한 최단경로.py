import sys
import heapq
input = sys.stdin.readline

def search(start, target):
    q = []
    distances = [sys.maxsize] * (n+1)
    distances[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        total, cur = heapq.heappop(q)
        for (neigh, distance) in graph[cur]:
            nd = total + distance
            if distances[neigh] > nd:
                distances[neigh] = nd
                heapq.heappush(q, (nd, neigh))
    return distances[target]

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

# 1 -> v1 -> v2 -> n
dist1 = search(1, v1) + search(v1, v2) + search(v2, n)
# 1 -> v2 -> v1 -> n
dist2 = search(1, v2) + search(v2, v1) + search(v1, n)

dist = min(dist1, dist2)
if dist >= sys.maxsize:
    print(-1)
else:
    print(dist)
