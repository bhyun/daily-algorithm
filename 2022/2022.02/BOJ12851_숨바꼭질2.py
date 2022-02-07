from collections import deque
import sys

n, k = map(int, input().split())
q = deque()

visited = [sys.maxsize] * 200000
q.append((0, n))
visited[n] = 0
answer = sys.maxsize
cnt = 0
while q:
    depth, cur = q.popleft()
    if depth > answer:
        continue

    if cur == k:
        if answer == depth:
            cnt += 1
        elif answer > depth:
            answer = depth
            cnt = 1
        continue

    if 0 <= cur-1 < 200000 and depth + 1 <= visited[cur-1]:
        visited[cur-1] = depth + 1
        q.append((depth + 1, cur - 1))
    if 0 <= cur+1 < 200000 and depth + 1 <= visited[cur+1]:
        visited[cur+1] = depth + 1
        q.append((depth + 1, cur + 1))
    if 0 <= cur*2 < 200000 and depth + 1 <= visited[cur*2]:
        visited[cur*2] = depth + 1
        q.append((depth + 1, cur * 2))
        
print(answer)
print(cnt)