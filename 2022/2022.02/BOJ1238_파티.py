import sys
import heapq
input = sys.stdin.readline

def dijstra(graph, distance, x):
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        dist, cur = heapq.heappop(q)

        if dist > distance[cur]:
            continue
        for neigh, cost in graph[cur]:
            if distance[neigh] > dist + cost:
                distance[neigh] = dist + cost
                heapq.heappush(q, (dist + cost, neigh))
    return distance

n, m, x = map(int, input().split())

origin = [[] for _ in range(n+1)]
reverse = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    origin[a].append((b, c))
    reverse[b].append((a, c))
origin_distance = [sys.maxsize] * (n+1)
reverse_distance = [sys.maxsize] * (n+1)

origin_distance = dijstra(origin, origin_distance, x)
reverse_distance = dijstra(reverse, reverse_distance, x)

answer = -sys.maxsize
for i in range(1, n+1):
    answer = max(answer, origin_distance[i] + reverse_distance[i])
print(answer)