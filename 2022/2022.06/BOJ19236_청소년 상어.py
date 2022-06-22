import sys
from collections import defaultdict, deque
from copy import deepcopy
input = sys.stdin.readline

def search(graph, target):
    for x in range(4):
        for y in range(4):
            if graph[x][y] == target:
                return True, x, y

    return False, -1, -1

def fish_move(graph, mapper):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    nm = deepcopy(mapper)

    for i in range(1, 17):
        check, x, y = search(graph, i)

        if check:
            cnt = 8
            while cnt:
                dir = nm[graph[x][y]]
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    # 이동한 위치에 상어가 있는 경우
                    if graph[nx][ny] == -1:
                        dir = (dir + 1) % 8
                        nm[graph[x][y]] = dir

                    # 이동한 위치가 빈칸이거나 물고기가 있는 경우
                    else:
                        graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                        break

                # 경계를 벗어나는 경우
                else:
                    dir = (dir + 1) % 8
                    nm[graph[x][y]] = dir

                cnt -= 1

    return graph, nm

graph = []
dir_mapper = defaultdict(int)
for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    graph.append([a1, a2, a3, a4])
    dir_mapper[a1] = b1 - 1
    dir_mapper[a2] = b2 - 1
    dir_mapper[a3] = b3 - 1
    dir_mapper[a4] = b4 - 1

q = deque()
eat = graph[0][0]
q.append((0, 0, dir_mapper[graph[0][0]], graph, dir_mapper, eat))
graph[0][0] = -1

answer = 0
while q:
    x, y, dir, graph, dir_mapper, eat = q.popleft()

    # 물고기 이동
    ng, nm = fish_move(graph, dir_mapper)

    # 상어 이동
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    cnt = 0
    for i in range(1, 4):
        nx = x + (dx[dir] * i)
        ny = y + (dy[dir] * i)

        if 0 <= nx < 4 and 0 <= ny < 4 and ng[nx][ny] > 0:
            eat_fish_id = ng[nx][ny] # 먹을 수 있는 물고기
            ng_copy = deepcopy(ng)
            ng_copy[x][y] = 0  # 현재 상어 위치를 0으로 만들기
            ng_copy[nx][ny] = -1  # 상어 위치 이동
            q.append((nx, ny, nm[eat_fish_id], ng_copy, nm, eat + eat_fish_id))

            cnt += 1

    # 더이상 이동할 수 있는 경로가 없음
    if cnt == 0:
        answer = max(answer, eat)

print(answer)

