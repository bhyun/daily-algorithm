import sys

def solution(n, s, a, b, fares):
    costs = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        costs[i][i] = 0

    for start, end, fare in fares:
        costs[start][end] = fare
        costs[end][start] = fare

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

    answer = costs[s][a] + costs[s][b]  # 합승 안함
    for i in range(1, n + 1):
        answer = min(answer, costs[s][i] + costs[i][a] + costs[i][b])  # i까지 합승 후 각자 이동

    return answer