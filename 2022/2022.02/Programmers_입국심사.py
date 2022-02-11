import sys

def solution(n, times):
    answer = sys.maxsize
    start, end = 1, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for time in times:
            result += mid // time

        if result >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer