import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n-1
value = sys.maxsize
answer = []
while start < end:
    result = arr[start] + arr[end]
    if abs(result) < abs(value):
        value = result
        answer = [arr[start], arr[end]]
    if result >= 0:
        end -= 1
    elif result < 0:
        start += 1

print(answer[0], answer[1])
