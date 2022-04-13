import sys
input = sys.stdin.readline

def search(index, array, type, bishop):
    global white_answer, black_answer

    if index >= len(array):
        if type == 0:
            black_answer = max(black_answer, bishop)
        else:
            white_answer = max(white_answer, bishop)
        return

    x, y = array[index]

    # select
    if board[x][y] == 1 and not issue1[x + y] and not issue2[n - 1 - x + y]:
        issue1[x + y] = 1
        issue2[n - 1 - x + y] = 1
        search(index + 1, array, type, bishop + 1)
        issue1[x + y] = 0
        issue2[n - 1 - x + y] = 0

    # not select
    search(index + 1, array, type, bishop)

n = int(input())
black = []
white = []
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if (i + j) % 2 == 0:
            black.append((i, j))
        else:
            white.append((i, j))

issue1 = [0] * (2 * n - 1)
issue2 = [0] * (2 * n - 1)
black_answer = -sys.maxsize
search(0, black, 0, 0)

white_answer = -sys.maxsize
search(0, white, 1, 0)

print(white_answer + black_answer)