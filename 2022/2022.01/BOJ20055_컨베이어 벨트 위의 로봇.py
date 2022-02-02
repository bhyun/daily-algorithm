import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
durability = deque(map(int, input().split()))
robot = deque([False]* n)
step = 1

while True:
    # 회전
    durability.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and durability[i+1] >= 1:
            robot[i+1] = True
            robot[i] = False
            durability[i+1] -= 1
    robot[-1] = False

    # 로봇 올리기
    if not robot[0] and durability[0] >= 1:
        robot[0] = True
        durability[0] -= 1

    if durability.count(0) >= k:
        break

    step += 1

print(step)

