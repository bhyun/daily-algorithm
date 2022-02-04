from collections import deque
import sys

def bfs(x, y, board):
    answer = sys.maxsize

    n = len(board)
    cost = [[sys.maxsize] * n for _ in range(n)]
    cost[x][y] = 0

    q = deque()
    q.append((x, y, -1, 0))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y, d, dist = q.popleft()

        if cost[x][y] < dist:
            continue
        if x == n - 1 and y == n - 1:
            answer = min(answer, dist)
            continue
        if dist > answer:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if i % 2 == 0:
                    nd = 0
                else:
                    nd = 1

                if d == -1 and dist + 100 <= cost[nx][ny]:
                    cost[nx][ny] = dist + 100
                    q.append((nx, ny, nd, dist + 100))
                elif d != nd and dist + 600 <= cost[nx][ny]:
                    cost[nx][ny] = dist + 600
                    q.append((nx, ny, nd, dist + 600))
                elif d == nd and dist + 100 <= cost[nx][ny]:
                    cost[nx][ny] = dist + 100
                    q.append((nx, ny, nd, dist + 100))
    return answer


def solution(board):
    answer = bfs(0, 0, board)
    return answer

# 마지막 테스트 통과못함
# 내일 재도전
print(solution(	[[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))