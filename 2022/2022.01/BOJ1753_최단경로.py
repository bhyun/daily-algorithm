import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (v + 1)
heap = []
heapq.heappush(heap, (0, start))
distance[start] = 0
while heap:
    dist, cur = heapq.heappop(heap)

    if distance[cur] < dist:
        continue

    for neigh, cost in graph[cur]:
        newCost = dist + cost
        if distance[neigh] > newCost:
            distance[neigh] = newCost
            heapq.heappush(heap, (distance[neigh], neigh))

for i in range(1, v+1):
    if i == start:
        print(0)
    elif distance[i] == INF:
        print("INF")
    else:
        print(distance[i])