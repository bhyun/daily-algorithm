from collections import deque
import sys

n, k = map(int, input().split())
q = deque()
q.append((n, 0))
seconds = sys.maxsize
cnt = 0
visited = [sys.maxsize] * 200000
visited[n] = 0

while q:
    cur, depth = q.popleft()

    if depth > seconds:
        continue

    if cur == k:
        if depth < seconds:
            seconds = depth
            cnt = 1
        elif depth == seconds:
            cnt += 1
        continue

    if 0 <= cur - 1 < 200000 and depth + 1 <= visited[cur - 1]:
        visited[cur - 1] = depth + 1
        q.append((cur - 1, depth + 1))

    if 0 <= cur + 1 < 200000 and depth + 1 <= visited[cur + 1]:
        visited[cur + 1] = depth + 1
        q.append((cur + 1, depth + 1))

    if 0 <= cur * 2 < 200000 and depth + 1 <= visited[cur * 2]:
        visited[cur * 2] = depth + 1
        q.append((cur * 2, depth + 1))

print(seconds)
print(cnt)
