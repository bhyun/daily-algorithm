import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

distance = [[sys.maxsize] * (n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 1
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            graph[i].append(j+1)
            distance[i][j+1] = 1
path = list(map(int, input().split()))

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(len(path)-1):
    cur, next = path[i], path[i+1]
    if distance[cur][next] == sys.maxsize:
        print("NO")
        break
else:
    print("YES")