import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
summary = [0]
for num in nums:
    summary.append(summary[-1] + num)

for _ in range(m):
    i, j = map(int, input().split())
    print(summary[j] - summary[i-1])