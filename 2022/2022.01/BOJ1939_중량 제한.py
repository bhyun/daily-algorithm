import sys
import heapq
input = sys.stdin.readline

def search(start):
    heap = []
    weights[start] = sys.maxsize
    heapq.heappush(heap, (-sys.maxsize, start))
    while heap:
        weight, cur = heapq.heappop(heap)
        weight = -weight

        if weights[cur] > weight:
            continue

        for (neigh, neighWeight) in graph[cur]:
            nw = min(weight, neighWeight)
            if weights[neigh] < nw:
                weights[neigh] = nw
                heapq.heappush(heap, (-weights[neigh], neigh))

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
weights = [0] * (n + 1)
search(v1)
print(weights[v2])


