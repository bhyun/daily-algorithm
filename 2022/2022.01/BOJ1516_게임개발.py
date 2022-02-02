n = int(input())
hours = [0] * (n+1)
parent = [[] for _ in range(n+1)]
for i in range(1, n+1):
    data = input().split()
    hour, nodes = int(data[0]), list(map(int, data[1:-1]))

    hours[i] = hour
    for node in nodes:
        parent[i].append(node)

calHour = [0] * (n+1)
visited = [False] * (n+1)

def search(cur):
    if not visited[cur]:
        visited[cur] = True

        if not parent[cur]: # 루트 노드
            calHour[cur] = hours[cur]

        for node in parent[cur]:
            search(node)
            calHour[cur] = max(calHour[cur], hours[cur] + calHour[node])

for i in range(1, n+1):
    if not visited[i]:
        search(i)

for i in range(1, n+1):
    print(calHour[i])
