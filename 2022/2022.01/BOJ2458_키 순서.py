import sys
input = sys.stdin.readline
n,m = map(int, input().split())

parent = [set() for _ in range(n+1)]
child = [set() for _ in range(n+1)]


for _ in range(m):
    a,b = map(int, input().split())
    parent[a].add(b)
    child[b].add(a)

for i in range(1,n+1):
    for j in child[i]:
        parent[j].update(parent[i])
    for j in parent[i]:
        child[j].update(child[i])

cnt = 0
for i in range(1,n+1):
    if len(parent[i])+len(child[i])==n-1:
        cnt += 1
print(cnt)
