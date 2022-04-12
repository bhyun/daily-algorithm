import sys
import heapq
input = sys.stdin.readline

def dijstra(node):
    q = []
    arr = [sys.maxsize] * (n+1)
    arr[node] = 0
    heapq.heappush(q, (0, node))

    while q:
        dist, cur = heapq.heappop(q)

        for next, next_dist in graph[cur]:
            if dist + next_dist < arr[next]:
                arr[next] = dist + next_dist
                heapq.heappush(q, (dist + next_dist, next))
    return arr

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

start = dijstra(1)
common = dijstra(v1)[v2]
end = dijstra(n)

path1, path2 = sys.maxsize, sys.maxsize
if start[v1] != sys.maxsize and end[v2] != sys.maxsize:
    path1 = start[v1] + common + end[v2]
if start[v2] != sys.maxsize and end[v1] != sys.maxsize:
    path2 = start[v2] + common + end[v1]

if path1 == sys.maxsize and path2 == sys.maxsize:
    print(-1)
else:
    print(min(path1, path2))