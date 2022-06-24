import sys

def complete_people(time, times):
    return sum(map(lambda x: time // x, times))

def solution(n, times):
    answer = sys.maxsize
    start, end = 1, max(times) * n
    while start <= end:
        mid = (start + end) // 2

        complete = complete_people(mid, times)
        if complete >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer

