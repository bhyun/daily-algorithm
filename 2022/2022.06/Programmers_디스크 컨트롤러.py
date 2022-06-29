import heapq


def solution(jobs):
    answer = 0

    cur = 0
    cnt = 0
    visited = [False] * (len(jobs))
    while True:

        if cnt == len(jobs):
            break

        q = []
        for i, job in enumerate(jobs):
            start, duration = job
            if start <= cur and not visited[i]:
                heapq.heappush(q, (duration, start, i))

        if not q:
            cur += 1
            continue

        time, start, id = heapq.heappop(q)
        visited[id] = True
        answer += time + (cur - start)

        cur += jobs[id][1]
        cnt += 1

    return answer // len(jobs)