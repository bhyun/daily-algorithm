import sys
input = sys.stdin.readline

def dfs(x, y, dir, col, path):
    global flag, ans_col, ans_path, ans_dir
    if len(path) == 5:
        fx = x + dx[dir]
        fy = y + dy[dir]
        bx = path[0][0] - dx[dir]
        by = path[0][1] - dy[dir]
        if 0 <= fx < 19 and 0 <= fy < 19 and board[fx][fy] == col:
            return
        if 0 <= bx < 10 and 0 <= by < 19 and board[bx][by] == col:
            return
        else:
            flag = True
            ans_col = col
            ans_dir = dir
            ans_path = path
        return


    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < 19 and 0 <= ny < 19:
        if board[nx][ny] == col:
            dfs(nx, ny, dir, col, path + [[nx, ny]])



board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]
flag = False
ans_col = 0
ans_dir = -1
ans_path = []
for i in range(15):
    for j in range(15):
        if board[i][j] != 0:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < 19 and 0 <= ny < 19:
                    if board[nx][ny] == board[i][j]:
                        dfs(nx, ny, k, board[i][j], [[i, j], [nx, ny]])

if flag:
   print(ans_col)
   if ans_dir == 3:
       print(ans_path[-1][0]+1, ans_path[-1][1]+1)
   else:
       print(ans_path[0][0] + 1, ans_path[0][1] + 1)

else:
    print(0)