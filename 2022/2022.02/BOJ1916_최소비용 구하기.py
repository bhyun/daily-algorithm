import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [sys.maxsize] * (n+1)
start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, node = heapq.heappop(q)

    if distance[node] < dist:
        continue

    for neigh, cost in graph[node]:
        if distance[neigh] > dist + cost:
            distance[neigh] = dist + cost
            heapq.heappush(q, (dist + cost, neigh))

print(distance[end])