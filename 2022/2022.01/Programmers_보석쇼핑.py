import sys
from collections import deque


def solution(gems):
    value = sys.maxsize
    answer = []

    start, end = 0, 0
    target = len(set(gems))

    mapper = {}
    temp = deque()
    temp.append(gems[start])
    mapper[gems[start]] = 1

    while end < len(gems) and start <= end:
        if len(mapper.keys()) == target:
            if end - start == value and start < answer[0]:
                answer = [start, end]
            elif end - start < value:
                value = end - start
                answer = [start, end]

            start += 1
            key = temp.popleft()
            mapper[key] -= 1
            if mapper[key] == 0:
                mapper.pop(key)
        else:
            end += 1
            if end >= len(gems):
                break
            if gems[end] not in mapper:
                mapper[gems[end]] = 1
            else:
                mapper[gems[end]] += 1
            temp.append(gems[end])
    return [answer[0] + 1, answer[1] + 1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))