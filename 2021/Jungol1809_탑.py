n = int(input())
tops = list(map(int, input().split()))

stack = []
answer = []
for i, top in enumerate(tops):

    while stack and stack[-1][1] < top:
        stack.pop()

    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][0] + 1)

    stack.append((i, top))

print(*answer)