# 다시풀기
import sys
import heapq

def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    q = []
    distance = [sys.maxsize] * (N+1)
    heapq.heappush(q, (0, 1))
    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for neigh, cost in graph[node]:
            if distance[neigh] > dist + cost and dist + cost <= K:
                distance[neigh] = dist + cost
                heapq.heappush(q, (dist + cost, neigh))

    for i in range(2, N+1):
        if distance[i] <= K:
            answer += 1
    return answer + 1

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))