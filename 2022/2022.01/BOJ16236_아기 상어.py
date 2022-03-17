# 다시 풀기
from collections import deque
import sys
input = sys.stdin.readline

def get_fish(shark_x, shark_y, shark):
    q = deque()
    q.append((0, shark_x, shark_y))

    visited = [[False] * n for _ in range(n)]
    visited[shark_x][shark_y] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    distance = sys.maxsize
    result_x = sys.maxsize
    result_y = sys.maxsize
    flag = False
    while q:
        dist, x, y = q.popleft()

        if dist > distance:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    q.append((dist + 1, nx, ny))
                elif graph[nx][ny] == shark:
                    q.append((dist + 1, nx, ny))
                elif graph[nx][ny] < shark:
                    if distance > dist + 1:
                        distance = dist + 1
                        result_x, result_y = nx, ny
                        flag = True

                    elif distance == dist + 1:
                        if result_x > nx:
                            result_x, result_y = nx, ny
                        elif result_x == nx and result_y > ny:
                            result_x, result_y = nx, ny

    return flag, distance, result_x, result_y

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

shark_x, shark_y = -1, -1
m = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] in [1, 2, 3, 4, 5, 6]:
            m += 1
        elif graph[i][j] == 9:
            shark_x, shark_y = i, j

graph[shark_x][shark_y] = 0

shark = 2
fish = 0
answer = 0
while m > 0:
    flag, distance, x, y = get_fish(shark_x, shark_y, shark)
    if flag:
        graph[x][y] = 0
        answer += distance
        shark_x = x
        shark_y = y
        fish += 1
        if fish == shark:
            shark += 1
            fish = 0
        m -= 1
    else:
        break

print(answer)