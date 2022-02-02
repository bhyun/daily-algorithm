import sys

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
d = [sys.maxsize] * (k+1)
d[0] = 0

for i in range(1, k+1):
    for j in coin:
        if i - j >= 0:
            d[i] = min(d[i], d[i-j] + 1)

if d[k] == sys.maxsize:
    print(-1)
else:
    print(d[k])