import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur):
    visited[cur] = True
    dp[cur][1] = resident[cur]
    for neigh in tree[cur]:
        if not visited[neigh]:
            dfs(neigh)
            dp[cur][1] += dp[neigh][0]
            dp[cur][0] += max(dp[neigh][0], dp[neigh][1])

n = int(input())
resident = [0] + list(map(int, input().split()))
visited = [False] * (n+1)
dp = [[0] * (2) for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
print(max(dp[1][0], dp[1][1]))