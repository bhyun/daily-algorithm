import sys
input = sys.stdin.readline

def ladder_game():
    for i in range(n):
        cur_row = 0
        cur_col = i
        while cur_row < h:
            if visited[cur_row][cur_col]:
                cur_col += 1
            elif visited[cur_row][cur_col-1]:
                cur_col -= 1

            cur_row += 1

        if cur_col != i:
            return False

    return True

def select(index, cnt):
    global answer

    if cnt >= 4:
        return

    if ladder_game():
        answer = min(answer, cnt)

    for i in range(index, h):
        for j in range(n-1):
            if visited[i][j]:
               continue

            if j-1 >= 0 and visited[i][j-1]:
                continue

            if j + 1 < n and visited[i][j+1]:
                continue

            visited[i][j] = True
            select(i, cnt + 1)
            visited[i][j] = False

answer = sys.maxsize
n, m, h = map(int, input().split())
visited = [[False] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    visited[a-1][b-1] = True

select(0, 0)
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)