# 다시 풀기

def solution(grid):
    answer = []

    n = len(grid)
    m = len(grid[0])

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    change_dir = {"R": [3, 0, 1, 2],
                  "S": [2, 3, 0, 1],
                  "L": [1, 2, 3, 0]}

    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            for d in range(4):
                if not visited[x][y][d]:
                    cnt = 0
                    while not visited[x][y][d]:
                        visited[x][y][d] = True
                        move = change_dir[grid[x][y]][d]
                        x = (x + direction[move][0]) % n
                        y = (y + direction[move][1]) % m
                        d = (move + 2) % 4
                        cnt += 1
                    answer.append(cnt)
    answer.sort()
    return answer

print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))