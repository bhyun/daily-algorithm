import sys

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # bfs 탐색
    def bfs(q):
        nonlocal answer
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while q:
            x, y, cnt = q.popleft()
            # 상대 진영에 도착 -> 거리 비교 시작
            if x == (n - 1) and y == (m - 1):
                answer = min(answer, cnt)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny, cnt + 1))

    answer = sys.maxsize
    # 내 캐릭터 위치에서 bfs 탐색 시작 (방문처리)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0, 1))  # x, y, cnt
    bfs(q)
    if answer == sys.maxsize:
        return -1
    return answer