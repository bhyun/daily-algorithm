def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 정렬
    sortFoods = []
    for i, time in enumerate(food_times):
        sortFoods.append([i, time])
    sortFoods.sort(key=lambda x: x[1])

    sec = 0
    idx = 0
    prev = 0

    while idx < len(sortFoods) and sec + (sortFoods[idx][1] - prev) * (len(sortFoods) - idx) <= k:
        sec += (sortFoods[idx][1] - prev) * (len(sortFoods) - idx)
        prev = sortFoods[idx][1]
        idx += 1

    # 남은 음식들
    sortFoods = sortFoods[idx:]
    for i in range(len(sortFoods)):
        sortFoods[i][1] -= prev
    sortFoods.sort()
    return sortFoods[(k - sec) % len(sortFoods)][0] + 1