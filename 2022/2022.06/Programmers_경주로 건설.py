import sys
from collections import deque


def solution(board):
    n = len(board)
    visited = [[[sys.maxsize] * 2 for _ in range(n)] for _ in range(n)]
    visited[0][0][0] = 0
    visited[0][0][1] = 0

    q = deque()
    q.append((0, 0, -1, 0))

    answer = sys.maxsize
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # d = -1: 첫이동
    # d = 0: 상하 이동
    # d = 1: 좌우 이동 
    while q:
        x, y, d, cost = q.popleft()

        if d != -1 and visited[x][y][d] < cost:
            continue

        if x == n - 1 and y == n - 1:
            answer = min(answer, cost)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if x != nx:
                nd = 0
            else:
                nd = 1

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                if d == -1:
                    visited[nx][ny][nd] = 100
                    q.append((nx, ny, nd, 100))
                elif d == nd and cost + 100 <= visited[nx][ny][nd]:
                    visited[nx][ny][nd] = cost + 100
                    q.append((nx, ny, nd, cost + 100))
                elif d != nd and cost + 600 <= visited[nx][ny][nd]:
                    visited[nx][ny][nd] = cost + 600
                    q.append((nx, ny, nd, cost + 600))

    return answer

