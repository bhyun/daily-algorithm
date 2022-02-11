t, w = map(int, input().split())
plum = [int(input()) for _ in range(t)]
dp = [[0]*t for _ in range(w+1)]

for i in range(w+1):
    if i % 2 == 0 and plum[0] == 1:
        dp[i][0] += 1
    elif i % 2 == 1 and plum[0] == 2:
        dp[i][0] += 1

for i in range(w+1):
    for j in range(1, t):
        if i == 0:
            if plum[j] == 1:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j - 1]
        elif (i % 2 == 0 and plum[j] == 1) or (i % 2 == 1 and plum[j] == 2):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i][j - 1])
answer = 0
for i in range(w+1):
    if dp[i][t-1] > answer:
        answer = dp[i][t-1]
print(answer)