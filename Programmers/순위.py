def solution(n, results):
    win = [set() for _ in range(n + 1)]  # i를 이긴 선수들
    lose = [set() for _ in range(n + 1)]  # i에게 진 선수들

    for w, l in results:
        win[l].add(w)
        lose[w].add(l)

    for i in range(1, n + 1):
        for j in win[i]:
            lose[j].update(lose[i])
        for j in lose[i]:
            win[j].update(win[j])
    print(lose)
    print(win)
    answer = 0
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer

print(solution(5, 	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))