import math

def solution(n, k):
    answer = []

    total = 0
    visited = [False] * (n + 1)
    trial = n - 1
    while len(answer) < n - 1:
        for i in range(1, n + 1):
            if not visited[i]:
                total += math.factorial(trial)
                if total >= k:
                    visited[i] = True
                    answer.append(i)
                    total -= math.factorial(trial)
                    break

        trial -= 1

    for i in range(1, n + 1):
        if not visited[i]:
            answer.append(i)
    return answer

