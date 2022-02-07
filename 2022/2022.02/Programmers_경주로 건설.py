from collections import deque
import sys

def bfs(x, y, board):
    n = len(board)
    q = deque()
    cost = [[[sys.maxsize] * 4 for _ in range(n)] for _ in range(n)]
    for i in range(4):
        q.append((0, 0, i, 0))
    answer = sys.maxsize

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, d, dist = q.popleft()

        if cost[x][y][d] < dist:
            continue

        if x == n - 1 and y == n - 1:
            answer = min(answer, dist)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if d == i and cost[nx][ny][i] > dist + 100:
                    cost[nx][ny][i] = dist + 100
                    q.append((nx, ny, i, dist + 100))
                elif d != i and cost[nx][ny][i] > dist + 600:
                    cost[nx][ny][i] = dist + 600
                    q.append((nx, ny, i, dist + 600))
    return answer

def solution(board):
    answer = bfs(0, 0, board)
    return answer