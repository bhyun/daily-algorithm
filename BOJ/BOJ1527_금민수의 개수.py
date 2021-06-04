from collections import deque

a, b = map(int, input().split())
q = deque()
q.append(0)
answer = []
while q:
    num = q.popleft()
    next1 = num * 10 + 4
    if  next1 <= b:
        q.append(next1)
        if next1 >= a:
            answer.append(next1)

    next2 = num * 10 + 7
    if next2 <= b:
        q.append(next2)
        if next2 >= a:
            answer.append(next2)
print(len(answer))