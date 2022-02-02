def solution(grid):
    r = len(grid)
    c = len(grid[0])
    move = {"S": [0, 1, 2, 3],
            "L": [3, 2, 0, 1],
            "R": [2, 3, 1, 0]}
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = [[[False for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    answer = []

    for i in range(r):
        for j in range(c):
            for k in range(4):
                if visited[i][j][k]:
                    continue

                x = i
                y = j
                cnt = 0
                while not visited[x][y][k]:
                    visited[x][y][k] = True
                    cnt += 1

                    cur = grid[x][y]
                    nx = (x + direction[move[cur][k]][0]) % r
                    ny = (y + direction[move[cur][k]][1]) % c
                    trans = move[cur][k]

                    x, y, k = nx, ny, trans

                answer.append(cnt)

    answer.sort()
    return answer

print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))