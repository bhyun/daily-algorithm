import sys
from collections import deque


def solution(board):
    n = len(board)
    visited = [[sys.maxsize] * n for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append((0, 0, 0, 0))  # x좌표, y좌표, cost, direction
    while q:
        x, y, cost, d = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if abs(nx - x) == 1:
                    nd = 1
                if abs(ny - y) == 1:
                    nd = 2

                if d == 0:
                    if cost + 100 <= visited[nx][ny]:
                        if nd == 1:
                            visited[nx][ny] = cost + 100
                            q.append((nx, ny, cost + 100, 1))
                        if nd == 2:
                            visited[nx][ny] = cost + 100
                            q.append((nx, ny, cost + 100, 2))
                else:
                    if nd != d:
                        if cost + 600 <= visited[nx][ny]:
                            visited[nx][ny] = cost + 600
                            q.append((nx, ny, cost + 600, nd))
                    elif nd == d:
                        if cost + 100 <= visited[nx][ny]:
                            visited[nx][ny] = cost + 100
                            q.append((nx, ny, cost + 100, nd))

    print(visited)
    return visited[n - 1][n - 1]