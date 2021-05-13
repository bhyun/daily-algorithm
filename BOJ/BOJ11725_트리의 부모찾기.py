import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9) #런타임 에러 방지


def dfs(start):
    for node in graph[start]:
        #if not visited[node]:
        if parent[node] == 0:
            parent[node] = start
            #visited[node] = True
            dfs(node)


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

parent = [0 for _ in range(n+1)]

dfs(1)
for i in range(2, n+1):
    print(parent[i])