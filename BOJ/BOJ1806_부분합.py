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
nums = list(map(int, input().split()))
answer = sys.maxsize

start, end = 0, 0
summary = nums[end]
while end < n and start < n and start <= end :
    if summary < s:
        end += 1
        if end < n:
            summary += nums[end]
    else:
        if answer > end - start:
            answer = end - start
        summary -= nums[start]
        start += 1


if answer == sys.maxsize:
    print(0)
else:
    print(answer + 1)
