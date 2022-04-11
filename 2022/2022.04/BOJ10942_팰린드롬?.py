import sys
input = sys.stdin.readline

n = int(input())
nums = input().split()

arr = [[0]*n for _ in range(n)]
# 홀수
for i in range(n):
    start, end = i-1, i+1
    string = nums[i]
    arr[i][i] = 1
    while start >= 0 and end < n:
        if nums[start] == nums[end]:
            arr[start][end] = 1
            start -= 1
            end += 1
        else:
            break
# 짝수
for i in range(n-1):
    if nums[i] == nums[i+1]:
        arr[i][i+1] = 1
        start, end = i-1, i+2
        while start >= 0 and end < n:
            if nums[start] == nums[end]:
                arr[start][end] = 1
                start -= 1
                end += 1
            else:
                break

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(arr[s-1][e-1])