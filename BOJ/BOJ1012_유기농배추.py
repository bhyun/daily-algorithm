# import sys
# sys.setrecursionlimit(50000)

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                dfs(nx, ny)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split()) # k: 배추의 수
        graph = [[0] * m for _ in range(n)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1

        visited = [[False]*m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and graph[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
        print(cnt)