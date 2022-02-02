def move(wheel, dir):
    # 시계방향
    if dir == 1:
        return wheels[wheel][-1] + wheels[wheel][:-1]
    else:
        return wheels[wheel][1:] + wheels[wheel][0]

def check(wheel, dir):
    moveIdx = [wheel]
    moveDir = [dir]
    originDir = dir

    # 오른쪽 방향 체크
    for i in range(wheel, 4):
        if wheels[i][2] != wheels[i+1][6]:
            moveIdx.append(i+1)
            dir = -dir
            moveDir.append(dir)
        else:
            break

    # 왼쪽 방향 체크
    dir = originDir
    for i in range(wheel, 1, -1):
        if wheels[i][6] != wheels[i - 1][2]:
            moveIdx.append(i-1)
            dir = -dir
            moveDir.append(dir)
        else:
            break

    for i in range(len(moveIdx)):
        wheels[moveIdx[i]] = move(moveIdx[i], moveDir[i])


wheels = [""]
for i in range(4):
    wheels.append(input())

n = int(input())
for _ in range(n):
    wheel, dir = map(int, input().split())
    check(wheel, dir)

print(int(wheels[1][0]) + (int(wheels[2][0]) * 2) + (int(wheels[3][0]) * 4) + (int(wheels[4][0]) * 8))
