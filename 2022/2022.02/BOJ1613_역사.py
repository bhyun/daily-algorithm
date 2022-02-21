import sys
input = sys.stdin.readline

n, k = map(int, input().split())
distance = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    distance[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if distance[a][b] == sys.maxsize and distance[b][a] == sys.maxsize:
        print(0)
    elif distance[a][b] != sys.maxsize:
        print(-1)
    elif distance[b][a] != sys.maxsize:
        print(1)
