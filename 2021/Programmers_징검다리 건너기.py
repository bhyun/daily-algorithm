def solution(stones, k):
    n = len(stones)
    answer = 0
    start, end = 0, max(stones)
    while start <= end:
        mid = (start + end) // 2
        rems = list(map(lambda x: 0 if x - mid < 0 else x - mid, stones))
        cnt = 0
        for rem in rems:
            if rem == 0:
                cnt += 1
                if cnt == k:
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            answer = mid + 1
            start = mid + 1
    return answer