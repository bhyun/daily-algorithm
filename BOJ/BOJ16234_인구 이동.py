import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    global u
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                visited[nx][ny] = True
                u.append([nx, ny])
                dfs(nx, ny)

def calculate(unions):
    for union in unions:
        total = 0
        for u in union:
            x, y = u
            total += graph[x][y]
        total //= len(union)
        for u in union:
            x, y = u
            graph[x][y] = total


n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False]*n for _ in range(n)]
unions = []
cnt = 0
while True:
    flag = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                u = []
                u.append([i, j])
                dfs(i, j)
                # u가 0이상일 때만 (연합이 발생한 경우)
                if len(u) > 1:
                    unions.append(u)
                    flag = True
    if flag:
        calculate(unions)
        cnt += 1
        # 초기화
        visited = [[False] * n for _ in range(n)]
        unions = []
    if not flag:
        break
print(cnt)
