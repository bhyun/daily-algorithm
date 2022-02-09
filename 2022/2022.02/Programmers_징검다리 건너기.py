def enable_to_cross(stones, k):
    cnt = 0
    for stone in stones:
        if stone < 0:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    answer = 0

    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2
        nstones = list(map(lambda x: x - mid, stones))

        if enable_to_cross(nstones, k):
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1

    return answer