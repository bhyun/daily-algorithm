import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cost = [[0] * m for _ in range(n)]
cost[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        temp = 0
        if i - 1 >= 0 and j - 1 >= 0:
            temp = max(temp, cost[i-1][j-1])
        if i - 1 >= 0:
            temp = max(temp, cost[i-1][j])
        if j - 1 >= 0:
            temp = max(temp, cost[i][j-1])
        cost[i][j] = temp + graph[i][j]
print(cost[n-1][m-1])

