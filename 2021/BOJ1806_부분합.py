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