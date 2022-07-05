def solution(m, n, board):
    answer = 0
    board = list(map(lambda x: list(x), board))

    while True:
        pop_list = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == "-":
                    continue
                standard = board[i][j]
                if board[i + 1][j] == standard and board[i][j + 1] == standard and board[i + 1][j + 1] == standard:
                    pop_list.add((i, j))
                    pop_list.add((i + 1, j))
                    pop_list.add((i, j + 1))
                    pop_list.add((i + 1, j + 1))

        # 이동할 수 없기 때문에 블록 멈춤
        if not pop_list:
            break

        pop_list = list(pop_list)
        pop_list.sort(key=lambda x: x[0]) # x값 기준으로 오름차순 탐색

        for x, y in pop_list:
            answer += 1
            for i in range(x, -1, -1): # x값부터 위로 올라가며 값 변경
                if i-1 < 0 or board[i-1][y] == "-":
                    board[i][y] = "-"
                    break
                board[i][y] = board[i-1][y]

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))