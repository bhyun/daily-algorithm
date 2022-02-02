n = int(input())
target = int(input())
graph = [[0]*n for _ in range(n)]

# 시작 위치
x, y = n//2, n//2
number = 1
graph[x][y] = number
number += 1

# 반복수
for i in range(n//2): # 0 - 1 - 2
    # up
    for j in range(2*i+1): # j: 횟수
        x -= 1
        graph[x][y] = number
        number += 1


    # right
    for j in range(2*i+1):
        y += 1
        graph[x][y] = number
        number += 1

    # down
    for j in range(2*(i+1)):
        x += 1
        graph[x][y] = number
        number += 1

    # left
    for j in range(2*(i+1)):
        y -= 1
        graph[x][y] = number
        number += 1

# # up
for i in range(2*(n//2)):
    x -= 1
    graph[x][y] = number
    number += 1

for g in graph:
    print(*g)

for i in range(n):
    for j in range(n):
        if graph[i][j] == target:
            print(i+1, j+1)
            break
