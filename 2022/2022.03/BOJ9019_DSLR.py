from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    visited = [False] * 10000
    q = deque()
    q.append((a, ""))
    while q:
        num, path = q.popleft()

        if num == b:
            print(path)
            break

        # D
        if num * 2 <= 9999 and not visited[num * 2]:
            visited[num * 2] = True
            q.append((num * 2, path + "D"))
        if num * 2 > 9999 and not visited[(num * 2) % 10000]:
            visited[(num * 2) % 10000] = True
            q.append(((num * 2) % 10000, path + "D"))

        # S
        if num - 1 >= 0 and not visited[num - 1]:
            visited[num - 1] = True
            q.append((num -1, path + "S"))
        if num - 1 < 0 and not visited[9999]:
            visited[9999] = True
            q.append((9999, path + "S"))

        # L
        temp = (num % 1000) * 10 + (num // 1000)
        if not visited[temp]:
            visited[temp] = True
            q.append((temp, path + "L"))

        # R
        temp = (num % 10) * 1000 + (num // 10)
        if not visited[temp]:
            visited[temp] = True
            q.append((temp, path + "R"))
