import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(k, late, absent):
    if k == n:
        if late < 2 and absent < 3: # 개근 성공
            return 1
        else: # 개근 실패
            return 0

    if not visited[k][late][absent] and late < 2 and absent < 3:
        visited[k][late][absent] = True
        dp[k][late][absent] += dfs(k+1, late, 0)
        dp[k][late][absent] += dfs(k+1, late+1, 0)
        dp[k][late][absent] += dfs(k+1, late, absent+1)
    return dp[k][late][absent]

n = int(input())
dp = [[[0] * 4 for _ in range(3)] for _ in range(n)]
visited = [[[False] * 4 for _ in range(3)] for _ in range(n)]
print((dfs(1, 0, 0) + dfs(1, 1, 0) + dfs(1, 0, 1)) % 1000000)