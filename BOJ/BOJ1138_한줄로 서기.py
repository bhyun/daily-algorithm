import sys

n = int(input())
heights = list(map(int, input().split()))
answer = [sys.maxsize] * n
for i, num in enumerate(heights):
    cnt = 0
    for j, ans in enumerate(answer):
        if cnt == num and answer[j] == sys.maxsize:
            answer[j] = i+1
            break
        if ans > i:
            cnt += 1
print(*answer)
