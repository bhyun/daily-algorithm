import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(node):
    for i in mapper[node]:
        if i in answer:
            answer.remove(i)

    for neigh in graph[node]:
        if not visited[neigh]:
            visited[neigh] = True
            dfs(neigh)

n, m = map(int, input().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
mapper = defaultdict(set)
answer = set(range(m))

truth_cnt, *truth = map(int, input().split())
for i in range(m):
    party_cnt, *member = map(int, input().split())
    for j in range(len(member)):
        n_member = member[:j] + member[j+1:]
        graph[member[j]].extend(n_member)
        mapper[member[j]].add(i)

for t in truth:
    if not visited[t]:
        visited[t] = True
        dfs(t)
print(len(answer))