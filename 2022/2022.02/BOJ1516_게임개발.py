# 다시 풀기

import sys
input = sys.stdin.readline

def dfs(node):
    if not visited[node]:
        visited[node] = True

        if not parent[node]:
            dp[node] = build_time[node]
            return

        for neighbor in parent[node]:
            dfs(neighbor)
            dp[node] = max(dp[node], build_time[node] + dp[neighbor])

n = int(input())
build_time = [0] * (n+1)
parent = [[] for _ in range(n+1)]
for i in range(1, n+1):
    data = list(map(int, input().split()))
    build_time[i] = data[0]
    parent[i] += data[1:-1]

dp = [0] * (n+1)
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

for i in range(1, n+1):
    print(dp[i])