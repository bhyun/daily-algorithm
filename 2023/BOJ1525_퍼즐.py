import sys
from collections import deque
input = sys.stdin.readline
answer = sys.maxsize

# input
string = ""
for _ in range(3):
    string += "".join(list(input().split()))

# visited, 큐 초기화
visited = {}
q = deque()
q.append((string, 0)) # 현재 string, 이동횟수
visited[string] = True

while q:
    current, move = q.popleft()

    # 종료 조건
    if current == "123456780":
        answer = min(answer, move)
        continue

    # 이동 가능한 방향 파악
    idx = current.index("0")
    if idx % 3 == 0:
        directions = [1, -3, 3] # 왼쪽 이동 불가
    elif idx % 3 == 2:
        directions = [-1, -3, 3] # 오른쪽 이동 불가
    else:
        directions = [-1, 1, -3, 3] # 모든 방향 이동 가능

    # 탐색
    for i in range(len(directions)):
        direction = directions[i]
        # 범위를 벗어나지 않는지 확인
        if idx + direction >= 0 and idx + direction < len(string):
            # swap
            new = list(current)
            new[idx + direction], new[idx] = new[idx], new[idx + direction]
            new_string = "".join(new)
            if new_string not in visited:
                visited[new_string] = True
                q.append((new_string, move + 1))

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)



