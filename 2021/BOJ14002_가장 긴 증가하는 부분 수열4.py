import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))

dp = [1] * n
arr = [[seq[i]] for i in range(n)]

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            arr[i] = arr[j] + [seq[i]]

length = 0
flag = 0
for i in range(n):
    if dp[i] > length:
        length = dp[i]
        flag = i
print(length)
print(*arr[flag])
