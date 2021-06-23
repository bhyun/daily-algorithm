import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
stack = []
result = 0
for i in range(n):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    result += len(stack)
    stack.append(i)

print(result)