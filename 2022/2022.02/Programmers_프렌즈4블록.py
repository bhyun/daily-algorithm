def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    answer = 0
    while True:
        pop_position = set()
        check = [[False] * n for _ in range(m)]
        flag = False
        for x in range(m - 1):
            for y in range(n - 1):
                if board[x][y] != '0' and board[x + 1][y] == board[x][y] and board[x][y + 1] == board[x][y] and board[x + 1][y + 1] == board[x][y]:
                    pop_position.add((x, y))
                    pop_position.add((x, y + 1))
                    pop_position.add((x + 1, y))
                    pop_position.add((x + 1, y + 1))
                    check[x][y] = True
                    check[x][y + 1] = True
                    check[x + 1][y] = True
                    check[x + 1][y + 1] = True
                    flag = True

        if not flag:
            break

        for y in range(n):
            new_col = []
            for x in range(m - 1, -1, -1):
                if not check[x][y]:
                    new_col.append(board[x][y])
            length = len(new_col)
            new_col.extend(['0'] * (m - length))
            for x in range(m):
                board[x][y] = new_col.pop()

        answer += len(pop_position)

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))