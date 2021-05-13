def solution(dirs):
    direction = ["U", "D", "R", "L"]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    x, y = 0, 0
    # 명령어대로 움직이면서 캐릭터가 처음 걸어본 길 길이 출력하기
    visited = []
    cnt = 0
    for dir in dirs:
        i = direction.index(dir)
        nx = x + dx[i]
        ny = y + dy[i]
        # 좌표면 경계 내부에 있는 지 확인하기
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 이미 길어간 길이 아닌지 확인하기
            if [x, y, nx, ny] not in visited or [nx, ny, x, y] not in visited:
                # 걸어간 길 visited에 저장하기
                visited.append([x, y, nx, ny])
                visited.append([nx, ny, x, y])
                cnt += 1
            x, y = nx, ny
    return cnt