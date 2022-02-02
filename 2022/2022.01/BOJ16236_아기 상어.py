import sys
input = sys.stdin.readline
from collections import deque

def check():
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < shark:
                return True
    return False

def bfs(originX, originY):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append(((originX, originY), 0))
    visited = [[False] * n for _ in range(n)]
    visited[originX][originY] = True

    candidates = []
    standard = sys.maxsize

    while q:
        (x, y), dist = q.popleft()
        if dist > standard:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] != 0 and graph[nx][ny] < shark:
                    if dist + 1 > standard:
                        continue
                    standard = dist + 1
                    candidates.append((nx, ny, dist + 1))
                elif graph[nx][ny] == 0 or graph[nx][ny] == shark:
                    q.append(((nx, ny), dist + 1))
                visited[nx][ny] = True

    if candidates:
        candidates.sort(key=lambda x: (x[0], x[1]))
        #print("후보: ", candidates)
        return candidates[0][0], candidates[0][1], candidates[0][2]
    return -1, -1, -1

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

shark = 2
second = 0
fish = 0

# 아기상어 위치 찾기
posFlag = True
for i in range(n):
    if not posFlag:
        break
    for j in range(n):
        if graph[i][j] == 9:
            posX, posY = i, j
            posFlag = False
            break

while True:
    # 먹을 수 있는 물고기가 없으면 탐색하지 않는다.
    if not check():
        print(second)
        break

    minX, minY, minDistance = bfs(posX, posY)
    #print("----minX, minY: ", minX, minY, "minDistance: ", minDistance )

    if minX == -1 and minY == -1:
        print(second)
        break

    fish += 1
    second += minDistance

    if fish == shark:
        shark += 1
        fish = 0
    #print("fish: ", fish, "shark: ", shark, "second: ", second)
    graph[posX][posY] = 0
    graph[minX][minY] = 9
    posX, posY = minX, minY
