### 재귀 - TLE
import sys

def solution(number, count):
    global answer
    if number == 1:
        if answer > count:
            answer = count
        return

    if number % 3 == 0:
        solution(number//3, count + 1)
    if number % 2 == 0:
        solution(number//2, count + 1)
    solution(number-1, count + 1)


num = int(input())
answer = sys.maxsize
solution(num, 0)
print(answer)


### 메모이제이션 - 통과
import sys

n = int(input())
dp = [sys.maxsize] * 1000001
dp[1] = 0
for i in range(2, 1000001):
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    dp[i] = min(dp[i], dp[i-1]+1)

print(dp[n])