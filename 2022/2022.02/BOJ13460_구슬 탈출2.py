import sys
from collections import deque
input = sys.stdin.readline

def first_move(rx, ry, bx, by, dir):
    if dir == 0:
        if rx >= bx:
            return 0 # R first
        return 1 # B first
    elif dir == 1:
        if rx <= bx:
            return 0
        return 1
    elif dir == 2:
        if ry >= by:
            return 0
        return 1
    else:
        if ry <= by:
            return 0
        return 1

def move(x, y, dx, dy, ox, oy):
    while True:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == "O":
                return True, nx, ny
            elif board[nx][ny] == "#" or (nx == ox and ny == oy):
                return False, x, y
            x = nx
            y = ny
        else:
            break
    return False, x, y

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 1))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            continue
        for i in range(4):
            first = first_move(rx, ry, bx, by, i)
            if first == 0:
                is_r_whole, nrx, nry = move(rx, ry, dx[i], dy[i], bx, by)
                is_b_whole, nbx, nby = move(bx, by, dx[i], dy[i], nrx, nry)
            else:
                is_b_whole, nbx, nby = move(bx, by, dx[i], dy[i], rx, ry)
                is_r_whole, nrx, nry = move(rx, ry, dx[i], dy[i], nbx, nby)

            if is_b_whole & is_r_whole:
                continue
            if is_b_whole:
                continue
            if is_r_whole:
                return cnt
            else:
                q.append((nrx, nry, nbx, nby, cnt + 1))
    return -1

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

rx, ry, bx, by = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            rx, ry = i, j
        elif board[i][j] == "B":
            bx, by = i, j
board[rx][ry] = "."
board[bx][by] = "."

print(bfs(rx, ry, bx, by))