import sys
input = sys.stdin.readline

r, c = map(int, input().split())
map = []
for _ in range(r):
    map.append(list(input()))

visited = [False] * 26
visited[ord('Z') - ord(map[0][0])] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = -sys.maxsize

def dfs(x, y):
    global answer
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[ord('Z') - ord(map[nx][ny])]:
            visited[ord('Z') - ord(map[nx][ny])] = True
            dfs(nx, ny)
            visited[ord('Z') - ord(map[nx][ny])] = False
        else:
            count += 1
            if count == 4:
                answer = max(answer, sum(visited))
                return


dfs(0, 0)
print(answer)


