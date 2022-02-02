def solution(n, computers):
    def dfs(computer):
        for i in range(n):
            if computers[computer][i] == 1 and not visited[i]:
                visited[i] = True
                dfs(i)

    visited = [False] * n
    cnt = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j)
                cnt += 1

    return cnt