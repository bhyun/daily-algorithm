import sys
input = sys.stdin.readline

def spread(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and before[nx][ny] != -1:
            after[nx][ny] += before[x][y] // 5
            cnt += 1
    after[x][y] += before[x][y] - ((before[x][y] // 5) * cnt)


def circulate(x, direction): # x - 로봇 청소기 위치 x좌표, direction - 로봇청소기의 위인지 아래인지
    if direction == 0: # 위
        # left
        for i in range(x, 0, -1):
           if before[i][0] == -1:
               continue
           before[i][0] = before[i-1][0]
        # top
        for i in range(1, c):
            before[0][i-1] = before[0][i]
        # right
        for i in range(x):
            before[i][c-1] = before[i+1][c-1]
        # bottom
        for i in range(c-1, 0, -1):
            if before[x][i-1] == -1:
                before[x][i] = 0
            else:
                before[x][i] = before[x][i-1]
    else:
        # left
        for i in range(x+1, r):
            if before[i-1][0] == -1:
                continue
            before[i-1][0] = before[i][0]
        # bottom
        for i in range(1, c):
            before[r-1][i-1] = before[r-1][i]
        # right
        for i in range(r-1, x, -1):
            before[i][c-1] = before[i-1][c-1]
        # top
        for i in range(c-1, 0, -1):
            if i == 1:
                before[x][i] = 0
            else:
                before[x][i] = before[x][i-1]


r, c, t = map(int, input().split())
before = []
for _ in range(r):
    before.append(list(map(int, input().split())))

pos = []
for i in range(r):
    if before[i][0] == -1:
        pos.append(i)

for i in range(t):
    after = [[0] * c for _ in range(r)]
    after[pos[0]][0] = -1
    after[pos[1]][0] = -1
    # 미세먼지 확산
    for i in range(r):
        for j in range(c):
            if before[i][j] != 0 and before[i][j] != -1:
                spread(i, j)
    before = after
    # 공기청정기 순환
    circulate(pos[0], 0)
    circulate(pos[1], 1)

ans = 0
for i in range(r):
    for j in range(c):
        if before[i][j] != -1 and before[i][j] != 0:
            ans += before[i][j]
print(ans)