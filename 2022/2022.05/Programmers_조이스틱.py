import sys

answer = sys.maxsize

def dfs(origin, name, index, n, visited, cnt, result):
    global answer

    if cnt == n:
        answer = min(answer, result)
        return

    nidx = index
    temp = 1
    while True:
        next = (nidx + 1) % n
        if not visited[next]:
            if ord(name[next]) > ord('N'):
                # 역방향
                addvalue = 26 - abs(ord(name[next]) - ord(origin[next]))
            else:
                # 정방향
                addvalue = ord(name[next]) - ord(origin[next])

            visited[next] = True
            dfs(origin, name, next, n, visited, cnt + 1, result + addvalue + temp)
            visited[next] = False
            break
        else:
            nidx = next
            temp += 1

    nidx = index
    temp = 1
    while True:
        next = (nidx - 1) % n
        if not visited[next]:
            if ord(name[next]) > ord('N'):
                # 역방향
                addvalue = 26 - abs(ord(name[next]) - ord(origin[next]))
            else:
                # 정방향
                addvalue = ord(name[next]) - ord(origin[next])

            visited[next] = True
            dfs(origin, name, next, n, visited, cnt + 1, result + addvalue + temp)
            visited[next] = False
            break
        else:
            nidx = next
            temp += 1

def solution(name):
    global answer

    n = len(name)
    origin = "A" * n

    visited = [False] * n
    visited[0] = True

    cnt = 0
    for i in range(1, n):
        if name[i] == "A":
            cnt += 1
            visited[i] = True

    if ord(name[0]) >= ord('N'):
        result = 26 - abs(ord(name[0]) - ord(origin[0]))
    else:
        result = ord(name[0]) - ord(origin[0])

    dfs(origin, name, 0, n, visited, cnt + 1, result)
    return answer