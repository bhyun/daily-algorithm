from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def move(id, x, y, dir, speed):
    if dir <= 2:
        speed = speed % ((r-1) * 2)
    else:
        speed = speed % ((c-1) * 2)

    while speed:
        if dir == 1:
            if x - 1 < 0:
                dir_mapper[id] = 2
                x += 1
            else:
                x -= 1

        elif dir == 2:
            if x + 1 >= r:
                dir_mapper[id] = 1
                x -= 1
            else:
                x += 1

        elif dir == 3:
            if y + 1 >= c:
                dir_mapper[id] = 4
                y -= 1
            else:
                y += 1

        elif dir == 4:
            if y - 1 < 0:
                dir_mapper[id] = 3
                y += 1
            else:
                y -= 1

        dir = dir_mapper[id]
        speed -= 1

    return x, y

r, c, m = map(int, input().split())
size_mapper = defaultdict(int)
dir_mapper = defaultdict(int)
speed_mapper = defaultdict(int)
q = []

for i in range(1, m+1):
    x, y, s, d, z = map(int, input().split())

    q.append((x-1, y-1, i))
    size_mapper[i] = z
    dir_mapper[i] = d
    speed_mapper[i] = s

# 상어 크기 순 정렬
q.sort(key=lambda x: size_mapper[x[2]])

answer = 0
for i in range(c):

    # 현재 열과 같은 열을 찾는다.
    tmp_index = sys.maxsize
    catch_id = 0
    for x, y, id in q:
        if y == i:
            if x < tmp_index:
                tmp_index = x
                catch_id = id

    if catch_id != 0:
        answer += size_mapper[catch_id]

    # 모든 상어를 이동시킨다.
    nq = deque()
    visited = [[False] * c for _ in range(r)]

    while q:
        x, y, id = q.pop()

        if id == catch_id:
            continue

        dir = dir_mapper[id]
        speed = speed_mapper[id]

        nx, ny = move(id, x, y, dir, speed)

        if not visited[nx][ny]:
            visited[nx][ny] = True
            nq.appendleft((nx, ny, id))

    q = nq

print(answer)
