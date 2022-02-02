def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    for move in moves:
        for i in range(n):
            val = board[i][move-1]
            if val != 0:
                # stack 비교
                if stack and stack[-1] == val:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(val)
                board[i][move-1] = 0
                break
    return answer