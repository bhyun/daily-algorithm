n = int(input())
tops = list(map(int, input().split()))
answer = [0] * n
stack = []


for i in range(len(tops)):
    top = tops[i]

    while stack and stack[-1][1] < top:
        stack.pop()

    while stack and stack[-1][1] > top:
        answer[i] = stack[-1][0] + 1
        break

    stack.append([i, tops[i]])

answer = list(map(str, answer))
print(" ".join(answer))