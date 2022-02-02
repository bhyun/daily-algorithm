from collections import deque

# 격자판 상태 정보 업데이트
def update(element):
    if element == -1:
        return 0
    elif element == 0:
        return 1
    elif element == 1:
        return 2
    elif element == 2:
        return 3
    else:
        return -1

def bomb(x, y):
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            graph[nx][ny] = -1


r, c, n = map(int, input().split())
graph = []
for _ in range(r):
    data = list(input())
    graph.append([-1 if x == '.' else 1 for x in data])

q = deque()

# n초 시간 경과
for k in range(n-1):
    for i in range(r):
        for j in range(c):
            graph[i][j] = update(graph[i][j])
            if graph[i][j] == 3:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        bomb(x, y)

# 상태값 -> 원래 값
for i in range(r):
    for j in range(c):
        if graph[i][j] != -1:
            graph[i][j] = 'O'
        else:
            graph[i][j] = '.'

for i in range(r):
    print("".join(graph[i]))

