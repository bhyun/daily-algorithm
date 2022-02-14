def move(board, x1, y1, x2, y2):
    origin = board[x1][y1]
    value = []
    value.append(origin)
    for i in range(x1 + 1, x2 + 1):
        board[i - 1][y1] = board[i][y1]
        value.append(board[i - 1][y1])
    for i in range(y1 + 1, y2 + 1):
        board[x2][i - 1] = board[x2][i]
        value.append(board[x2][i - 1])
    for i in range(x2 - 1, x1 - 1, -1):
        board[i + 1][y2] = board[i][y2]
        value.append(board[i + 1][y2])
    for i in range(y2 - 1, y1, -1):
        board[x1][i + 1] = board[x1][i]
        value.append(board[x1][i + 1])
    board[x1][y1 + 1] = origin
    return board, min(value)

def solution(rows, columns, queries):
    answer = []
    temp = 1
    board = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = temp
            temp += 1

    for x1, y1, x2, y2 in queries:
        board, min_value = move(board, x1 - 1, y1 - 1, x2 - 1, y2 - 1)
        answer.append(min_value)
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))