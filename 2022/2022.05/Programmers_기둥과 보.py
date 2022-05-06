def check(x, y, type, columns, beams):
    # 기둥인 경우
    if type == 0:
        if y == 0 or (x, y) in beams or (x - 1, y) in beams or (x, y - 1) in columns:
            return True
    # 보인 경우
    else:
        if (x, y - 1) in columns or (x + 1, y - 1) in columns or ((x - 1, y) in beams and (x + 1, y) in beams):
            return True
    return False

def solution(n, build_frame):
    answer = []

    columns = []
    beams = []
    for x, y, a, b in build_frame:
        # 삭제하는 경우
        if b == 0:
            # 기둥
            if a == 0:
                columns.remove((x, y))

                dx = [-1, 0, 0]
                dy = [1, 1, 1]
                dtype = [1, 1, 0]
                for i in range(3):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    type = dtype[i]
                    if (nx, ny, type) in answer:
                        if not check(nx, ny, type, columns, beams):
                            columns.append((x, y))
                            break
                else:
                    answer.remove((x, y, 0))
            # 보
            else:
                beams.remove((x, y))

                dx = [0, 1, -1, 1]
                dy = [0, 0, 0, 0]
                dtype = [0, 0, 1, 1]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    type = dtype[i]
                    if (nx, ny, type) in answer:
                        if not check(nx, ny, type, columns, beams):
                            beams.append((x, y))
                            break
                else:
                    answer.remove((x, y, 1))
        # 설치하는 경우
        if b == 1:
            # 기둥
            if a == 0:
                if check(x, y, a, columns, beams):
                    columns.append((x, y))
                    answer.append((x, y, 0))
            # 보
            else:
                if check(x, y, a, columns, beams):
                    beams.append((x, y))
                    answer.append((x, y, 1))

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer