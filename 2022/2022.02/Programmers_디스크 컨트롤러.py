import heapq

def solution(jobs):
    answer = 0

    jobs.sort(key=lambda x: x[0])
    q = []
    time = 0
    completed = 0
    visited = [False] * len(jobs)
    while completed < len(jobs):
        for i, job in enumerate(jobs):
            if not visited[i] and job[0] <= time:
                visited[i] = True
                heapq.heappush(q, (job[1], job[0]))

        if q:
            duration, start = heapq.heappop(q)
            time += duration
            answer += (time - start)
            completed += 1
        else:
            time += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]	))