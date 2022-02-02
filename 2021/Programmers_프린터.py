from collections import deque

def solution(priorities, location):
    n = len(priorities)
    index = deque(range(n))
    q = deque(priorities)
    answer = []
    while q:
        val = q.popleft()
        idx = index.popleft()
        for p in q:
            if val < p:
                q.append(val)
                index.append(idx)
                break
        else:
            answer.append(idx)
            if idx == location:
                return len(answer)