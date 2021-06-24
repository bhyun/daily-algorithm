import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1)]
for _ in range(n):
    data = [0] + list(map(int, input().split()))
    graph.append(data)

# 구간합 구하기
for i in range(1, n+1):
    for j in range(1, n):
        graph[i][j+1] += graph[i][j]

for i in range(1, n):
    for j in range(1, n+1):
        graph[i+1][j] += graph[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(graph[x2][y2]-graph[x1-1][y2]-graph[x2][y1-1]+graph[x1-1][y1-1])