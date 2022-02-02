import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

stack = []
ans = [0] * n

for i, a in enumerate(A):
    while stack and stack[-1][1] < a:
        ans[stack.pop()[0]] = a
    stack.append((i, a))

while stack:
    i, a = stack.pop()
    ans[i] = -1

print(*ans)
