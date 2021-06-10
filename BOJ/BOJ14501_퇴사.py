### 완전 탐색
from collections import deque

n = int(input())
t = [] # 상담을 했을 때 걸리는 시간
p = [] # 상담을 했을 때 받을 수 있는 돈
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

q = deque()
answer = 0

for i in range(n):
    if i + t[i] <= n:
        q.append((i + t[i], p[i]))  #상담 후 상담이 가능한 첫 날짜, 누적 금액

while q:
    day, mon = q.popleft()

    if mon > answer:
        answer = mon

    # 상담이 가능한 날짜부터 세기
    for i in range(day, n):
        if i + t[i] <= n:
            q.append((i + t[i], mon + p[i]))

print(answer)

### Dynamic Programming
n = int(input())
t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
d = [0] * (n+1)
for i in range(n):
    if i + t[i] <= n:
        d[i + t[i]] = max(d[i + t[i]], d[i] + p[i])
        d[i + t[i]] = max(d[i + t[i]] , max(d[:i+1]) + p[i])
print(max(d))