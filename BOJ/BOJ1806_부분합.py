### TLE
# import copy
# import sys
# input = sys.stdin.readline
#
# n, s = map(int, input().split())
# nums = list(map(int, input().split()))
# answer = 0
#
# dp = copy.deepcopy(nums)
# flag = False
#
# # 길이 2 ~ n
# for length in range(2, n+1):
#     for i in range(n-length+1):
#         dp[i] = dp[i] + nums[i+length-1]
#         if dp[i] >= s:
#             flag = True
#             break
#
#     if flag:
#         answer = length
#         break
#
# print(answer)

### Two pointer
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
summary = arr[start]
answer = sys.maxsize

flag = False

while start <= end:
    if summary < s:
        if end < n-1:
            end += 1
            summary += arr[end]
        else:
            break
    else:
        flag = True
        answer = min(answer, end - start + 1)
        summary -= arr[start]
        start += 1

if flag:
    print(answer)
else:
    print(0)