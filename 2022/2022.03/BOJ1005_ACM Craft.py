from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    target = int(input())

    roots = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            roots.append(i)

    cost = [0] * (n+1)
    q = deque()
    for root in roots:
        q.append(root)
        cost[root] = time[root]

    while q:
        node = q.popleft()

        for neigh in graph[node]:
            cost[neigh] = max(cost[neigh], time[neigh] + cost[node])
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                q.append(neigh)
    print(cost[target])