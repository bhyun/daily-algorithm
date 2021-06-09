import sys
input = sys.stdin.readline

def dfs(x, y, cnt, summary):
    global answer

    if cnt == k:
        if summary > answer:
            answer = summary
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            # (i, j)에서 인접한 위치 탐색
            if i == x and j == y:
                continue
            flag = True
            for r in range(4):
                nx = i + dx[r]
                ny = j + dy[r]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        flag = False
                        break
            if flag:
                visited[i][j] = True
                dfs(i, j, cnt + 1, summary + board[i][j])
                visited[i][j] = False


n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]  # __#
answer = -sys.maxsize

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
print(answer)