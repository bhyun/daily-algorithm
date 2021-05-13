def solution(land):
    n = len(land)
    # 1, 2, 3, 5
    # 10, 11, 12, 11
    # 16, 15, 13, 13
    d = [[0] * 4 for _ in range(n)]
    # 첫번째 행 초기화
    for j in range(4):
        d[0][j] = land[0][j]
    # 나머지 행 탐색
    for i in range(1, n):
        d[i][0] = max(d[i - 1][1], d[i - 1][2], d[i - 1][3]) + land[i][0]
        d[i][1] = max(d[i - 1][0], d[i - 1][2], d[i - 1][3]) + land[i][1]
        d[i][2] = max(d[i - 1][0], d[i - 1][1], d[i - 1][3]) + land[i][2]
        d[i][3] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2]) + land[i][3]
    return max(d[n - 1])