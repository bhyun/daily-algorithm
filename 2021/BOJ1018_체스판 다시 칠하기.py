import sys
input = sys.stdin.readline

def check(x, y):

    # 1. start - white
    col = "W"
    white_cnt = 0 # white로 다시 칠해야할 셀의 개수
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) % 2 == 0 and boards[i][j] != col:
                white_cnt += 1
            elif (i+j) % 2 != 0 and boards[i][j] == col:
                white_cnt += 1

    # 2. start - black
    col = "B"
    black_cnt = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) % 2 == 0 and boards[i][j] != col:
                black_cnt += 1
            elif (i+j) % 2 != 0 and boards[i][j] == col:
                black_cnt += 1

    return min(white_cnt, black_cnt)


n, m = map(int, input().split())
boards = []
for _ in range(n):
    boards.append(list(input()))

result = sys.maxsize
for i in range(n-7):
    for j in range(m-7):
        cnt = check(i, j)
        if result > cnt:
            result = cnt

print(result)