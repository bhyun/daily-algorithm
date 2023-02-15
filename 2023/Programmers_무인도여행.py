from collections import deque

def solution(maps):
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        ans = int(maps[x][y])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != "X" and not visited[nx][ny]:
                        ans += int(maps[nx][ny])
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return ans

    n, m = len(maps), len(maps[0])
    answer = []
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            tmp = 0
            if maps[i][j] != "X" and not visited[i][j]:
                tmp += int(maps[i][j])
                visited[i][j] = True
                answer.append(bfs(i, j))

    if len(answer) == 0:
        return [-1]
    return sorted(answer)