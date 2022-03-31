import heapq

def solution(jobs):
    n = len(jobs)

    jobs.sort(key=lambda x: (x[0], x[1]))

    seconds = 0
    answer = 0
    visited = [False] * n

    while True:
        controller = []

        for i in range(n):
            start, duration = jobs[i][0], jobs[i][1]
            if not visited[i] and start <= seconds:
                heapq.heappush(controller, (seconds + duration, i))

        # 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리
        if not controller:
            for i in range(n):
                if not visited[i]:
                    start, duration = jobs[i][0], jobs[i][1]
                    heapq.heappush(controller, (start + duration, i))
                    break

        if controller:
            time, cur = heapq.heappop(controller)
            visited[cur] = True
            answer += time - jobs[cur][0]
            seconds = time
        else:
            break

    return answer // n