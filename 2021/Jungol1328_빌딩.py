import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
answer = [0] * n
stack = []
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack[-1]] = i + 1
        stack.pop()

    stack.append(i)

for ans in answer:
    print(ans)
