import sys
from collections import deque
from copy import deepcopy

def solution(picks, minerals):
    answer = sys.maxsize
    mineral_dict = {"diamond": 0, "iron": 1, "stone": 2}

    # 곡괭이-광물 당 피로도
    pirodo = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

    q = deque()
    # 모든 곡괭이 타입을 queue에 담기
    for i, pick in enumerate(picks):
        if pick > 0:
            new_picks = deepcopy(picks)
            new_picks[i] -= 1
            q.append((i, 0, new_picks, 0, 0))  # 현재 곡괭이 인덱스, 현재 곡괭이 사용도, 곡괭이 현황, 탐색중인 mineral index, 누적 피로도

    while q:
        cur_pick_index, cur_pick_use, cur_picks, mineral_index, ans = q.popleft()

        # 누적 피로도 중간값이 answer보다 큰 경우는 더이상 탐색하지 않음
        if ans > answer:
            continue

        # 종료 조건 no.1
        if mineral_index >= len(minerals):
            answer = min(ans, answer)
            continue

        if cur_pick_use < 5:
            if mineral_index < len(minerals):
                piro = pirodo[cur_pick_index][mineral_dict[minerals[mineral_index]]]
                q.append((cur_pick_index, cur_pick_use + 1, cur_picks, mineral_index + 1, ans + piro))

        elif cur_pick_use == 5:
            flag = False
            for i, pick in enumerate(cur_picks):
                if pick > 0 and mineral_index < len(minerals):
                    new_picks = deepcopy(cur_picks)
                    new_picks[i] -= 1
                    q.append((i, 0, new_picks, mineral_index, ans))
                    flag = True

            if not flag:
                # 종료 조건 no.2
                answer = min(answer, ans)
                continue


    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])) # 12
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])) # 50