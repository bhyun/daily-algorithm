import heapq


def solution(scoville, K):
    h = []
    for s in scoville:
        heapq.heappush(h, s)
    cnt = 0
    while True:
        food1 = heapq.heappop(h)
        if not h and food1 <= K:
            return -1
        if food1 >= K:
            return cnt

        food2 = heapq.heappop(h)
        heapq.heappush(h, food1 + (food2 * 2))
        cnt += 1
    return cnt