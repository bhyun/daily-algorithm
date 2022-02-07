from collections import deque
answer = 0

def bfs(computers, computer, visited):
    global answer

    n = len(computers)
    q = deque()
    q.append(computer)

    while q:
        cur = q.popleft()
        for i in range(n):
            if i != cur and computers[cur][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
    answer += 1

def solution(n, computers):
    global answer
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
    return answer