def solution(targets):
    answer = 1
    targets.sort(key=lambda x: (x[1])) #두번째(end)값을 기준으로 정렬
    key = targets[0][1]

    for i in range(1, len(targets)):
        x = targets[i][0]
        if key <= x: # 요격 미사일의 첫번째(start)값이 key보다 크면 key 갱신, answer + 1
            key = targets[i][1]
            answer += 1

    return answer