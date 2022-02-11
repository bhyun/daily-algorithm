from collections import deque

def make_graph(n, rank):
    indegree = [0] * (n+1)
    child = [[] for _ in range(n+1)]
    for i in range(n-1):
        for j in range(i+1, n):
            child[rank[i]].append(rank[j])
            indegree[rank[j]] += 1
    return child, indegree

def change_child(child, indegree, a, b):
    if a in child[b]:
        child[b].remove(a)
        indegree[a] -= 1
        child[a].append(b)
        indegree[b] += 1
    else:
        child[a].remove(b)
        indegree[b] -= 1
        child[b].append(a)
        indegree[a] += 1
    return child, indegree

def search(n, child, indegree):
    q = deque()
    visited = [False] * (n+1)
    answer = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            visited[i] = True
            answer.append(i)
            q.append(i)

    while q:
        node = q.popleft()
        for neigh in child[node]:
            if not visited[neigh]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    visited[neigh] = True
                    answer.append(neigh)
                    q.append(neigh)

    if sum(visited[1:]) != n:
        print("IMPOSSIBLE")
    else:
        print(*answer)

t = int(input())
for _ in range(t):
    n = int(input())
    rank = list(map(int, input().split()))
    child, indegree = make_graph(n, rank)
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        child, indegree = change_child(child, indegree, a, b)
    search(n, child, indegree)