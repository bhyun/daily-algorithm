from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

chickens = []
homes = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append((i, j))
        elif graph[i][j] == 1:
            homes.append((i, j))


cases = list(combinations(chickens, m))

answer = sys.maxsize
for case in cases:
    total = 0
    for home in homes:
        dist = sys.maxsize
        for c in case:
            dist = min(dist, abs(home[0] - c[0]) + abs(home[1] - c[1]))
        total += dist
    answer = min(answer, total)
print(answer)