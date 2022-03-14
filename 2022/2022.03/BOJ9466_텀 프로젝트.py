import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    global answer
    cycle.append(node)
    visited[node] = True

    if not visited[data[node]]:
        dfs(data[node])
    else:
        if data[node] in cycle:
            answer.update(set(cycle[cycle.index(data[node]):]))
        return

t = int(input())
for _ in range(t):
    n = int(input())

    visited = [False] * (n+1)
    data = [0] + list(map(int, input().split()))
    answer = set()

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - len(answer))