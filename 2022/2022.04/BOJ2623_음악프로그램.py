import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

child = [[] for _ in range(n+1)]
visited = [False] * (n+1)
indegree = [0] * (n+1)
for _ in range(m):
    cnt, *singers = list(map(int, input().split()))
    for i in range(len(singers)-1):
        cur, next = singers[i], singers[i+1]
        child[cur].append(next)
        indegree[next] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        visited[i] = True
        q.append(i)

answer = []
while q:
    cur = q.popleft()
    answer.append(cur)

    for node in child[cur]:
        if not visited[node]:
            indegree[node] -= 1
            if indegree[node] == 0:
                visited[node] = True
                q.append(node)

if sum(visited) != n:
    print(0)
else:
    for i in answer:
        print(i)