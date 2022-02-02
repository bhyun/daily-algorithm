from collections import deque
import math


def solution(progresses, speeds):
    days = deque()
    answer = []

    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        if not days:
            days.append(day)
        else:
            if days[0] >= day:
                days.append(day)
            else:
                answer.append(len(days))
                days = [day]
    answer.append(len(days))
    return answer