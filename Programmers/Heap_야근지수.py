import heapq


def solution(n, works):
    h = []
    for work in works:
        heapq.heappush(h, -work)

    while n > 0:
        work = heapq.heappop(h)
        if work == 0:
            heapq.heappush(h, work)
        else:
            heapq.heappush(h, work + 1)
        n -= 1
    answer = 0
    while h:
        work = heapq.heappop(h)
        answer += (-work) ** 2
    return answer