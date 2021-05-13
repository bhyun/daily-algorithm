def solution(triangle):
    n = len(triangle)
    dp = [[0]*i for i in range(1, n+1)]
    for i in range(n):
        for j in range(i+1):
            if i == 0:
                dp[i][j] = triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    return max(dp[-1])