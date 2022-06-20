import sys
from collections import deque
input = sys.stdin.readline

def spring_summer():
    for i in range(n):
        for j in range(n):
            cnt = len(live_trees[i][j])
            death_tree = 0
            while cnt:
                age = live_trees[i][j].popleft()
                if foods[i][j] >= age:
                    foods[i][j] -= age
                    live_trees[i][j].append(age + 1)
                else:
                    death_tree += age // 2

                cnt -= 1

            foods[i][j] += death_tree

def fall():
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(n):
        for j in range(n):
            for age in live_trees[i][j]:
                if age % 5 == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            live_trees[nx][ny].appendleft(1)

def winter():
    for i in range(n):
        for j in range(n):
            foods[i][j] += origin[i][j]

n, m, k = map(int, input().split())
origin = []
for _ in range(n):
    origin.append(list(map(int, input().split())))
foods = [[5] * n for _ in range(n)]

live_trees = [[deque() for _ in range(n) ] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    live_trees[x-1][y-1].append(z)

for _ in range(k):
    spring_summer()
    fall()
    winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(live_trees[i][j])
print(answer)

