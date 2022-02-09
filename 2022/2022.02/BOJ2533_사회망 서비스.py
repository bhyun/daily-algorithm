# 다시 풀어보기
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for neigh in tree[node]:
        if not visited[neigh]:
            dfs(neigh)  # 가장 말단 노드까지 이동
            dp[node][0] += dp[neigh][1]
            dp[node][1] += min(dp[neigh][0], dp[neigh][1])

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
dp = [[0, 1] for _ in range(n+1)]
dfs(1)
print(min(dp[1][0], dp[1][1]))