from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
answer = []
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    answer.append(str(node))

    for neigh in graph[node]:
        indegree[neigh] -= 1
        if indegree[neigh] == 0:
            q.append(neigh)

print(" ".join(answer))
