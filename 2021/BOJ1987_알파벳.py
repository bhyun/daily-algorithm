import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    global answer

    answer = max(answer, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not alpha[ord(board[nx][ny]) - ord('A')]:
                alpha[ord(board[nx][ny]) - ord('A')] = True
                dfs(nx, ny, cnt + 1)
                alpha[ord(board[nx][ny]) - ord('A')] = False

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
alpha = [False] * 26
answer = 0

char = board[0][0]
alpha[ord(char) - ord('A')] = True
dfs(0, 0, 1)
print(answer)