import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(weight):
    q = deque()
    visited = [False] * (n+1)
    visited[s] = True
    q.append(s)
    while q:
        cur = q.popleft()

        if cur == e:
            return True

        dict = graph[cur]
        for k, v in dict.items():
            if not visited[k] and v >= weight:
                visited[k] = True
                q.append(k)
    return False

n, m = map(int, input().split())
graph = []
for _ in range(n+1):
    graph.append(defaultdict(int))

for _ in range(m):
    a, b, c = map(int, input().split())
    if c > graph[a][b]:
        graph[a][b] = c
    if c > graph[b][a]:
        graph[b][a] = c

s, e = map(int, input().split())
answer = -sys.maxsize
start, end = 1, 1000000000
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)