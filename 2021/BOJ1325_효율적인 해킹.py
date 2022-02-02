import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

coms = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    coms[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited = [False] * (n+1)
    visited[x] = True
    cnt = 1
    while q:
        com = q.popleft()
        for next in coms[com]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                q.append(next)
    return cnt

val = 0
answer = [0] * (n+1)
for i in range(1, n+1):
    answer[i] = bfs(i)

for i in range(1, n+1):
    if answer[i] == max(answer):
        print(i, end=" ")
