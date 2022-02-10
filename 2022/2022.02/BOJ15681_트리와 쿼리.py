import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    for neigh in tree[node]:
        if not visited[neigh]:
            visited[node] = True
            dfs(neigh)
            dp[node] += dp[neigh]

n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n+1)
dp = [1] * (n+1)
visited[r] = True
dfs(r)
for _ in range(q):
    u = int(input())
    print(dp[u])
