def isPossible(place, x, y, nx, ny):
    checks = {
        (-1, -1): [(-1, 0), (0, -1)],
        (-1, 1): [(-1, 0), (0, 1)],
        (1, -1): [(0, -1), (1, 0)],
        (1, 1): [(0, 1), (1, 0)],
        (-2, 0): [(-1, 0)],
        (0, -2): [(0, -1)],
        (0, 2): [(0, 1)],
        (2, 0): [(1, 0)]
    }

    if (nx, ny) in checks:
        for (dx, dy) in checks[(nx,ny)]:
            mx = x + dx
            my = y + dy
            if 0 <= mx < 5 and 0 <= my < 5 and place[mx][my] != "X":
                return False
    else:
        # 거리 1이하이기 때문에 거리두기 안된것
        return False
    return True


def check(place, x, y):
    dx = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2]
    dy = [0, -1, 0, 1, -2, -1, 1, 2, -1, 0, 1, 0]

    for i in range(12):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] == "P":
                if not isPossible(place, x, y, dx[i], dy[i]):
                    return False
    return True


def solution(places):
    answer = [1] * 5

    for k, place in enumerate(places):
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if not check(place, i, j):
                        answer[k] = 0
    return answer
