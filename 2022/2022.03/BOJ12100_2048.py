import sys
from copy import deepcopy
input = sys.stdin.readline

def up(board):
    for i in range(n):
        prev, cur = 0, 1
        while cur < n:
            if board[cur][i]:
                temp = board[cur][i]
                board[cur][i] = 0
                if board[prev][i] == temp:
                    board[prev][i] = temp * 2
                    prev += 1
                elif board[prev][i] == 0:
                    board[prev][i] = temp
                else:
                    prev += 1
                    board[prev][i] = temp
            cur += 1

    return board

def down(board):
    for i in range(n):
        prev, cur = n-1, n-2
        while cur >= 0:
            if board[cur][i]:
                temp = board[cur][i]
                board[cur][i] = 0
                if board[prev][i] == temp:
                    board[prev][i] = temp * 2
                    prev -= 1
                elif board[prev][i] == 0:
                    board[prev][i] = temp
                else:
                    prev -= 1
                    board[prev][i] = temp
            cur -= 1

    return board

def right(board):
    for i in range(n):
        prev, cur = n-1, n-2
        while cur >= 0:
            if board[i][cur]:
                temp = board[i][cur]
                board[i][cur] = 0
                if board[i][prev] == temp:
                    board[i][prev] = temp * 2
                    prev -= 1
                elif board[i][prev] == 0:
                    board[i][prev] = temp
                else:
                    prev -= 1
                    board[i][prev] = temp
            cur -= 1

    return board

def left(board):
    for i in range(n):
        prev, cur = 0, 1
        while cur < n:
            if board[i][cur]:
                temp = board[i][cur]
                board[i][cur] = 0
                if board[i][prev] == temp:
                    board[i][prev] = temp * 2
                    prev += 1
                elif board[i][prev] == 0:
                    board[i][prev] = temp
                else:
                    prev += 1
                    board[i][prev] = temp
            cur += 1

    return board

def dfs(board, cnt):
    global answer

    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return

    new_board = deepcopy(board)
    dfs(up(new_board), cnt + 1)

    new_board = deepcopy(board)
    dfs(down(new_board), cnt + 1)

    new_board = deepcopy(board)
    dfs(right(new_board), cnt + 1)

    new_board = deepcopy(board)
    dfs(left(new_board), cnt + 1)

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
dfs(board, 0)
print(answer)