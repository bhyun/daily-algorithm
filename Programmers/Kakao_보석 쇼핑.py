import sys


def solution(gems):
    kinds = len(set(gems))  # 보석의 종류 개수
    n = len(gems)
    d = {}
    answer = []
    diff = sys.maxsize
    l, r = 0, 0
    while l <= n and r <= n:
        if len(d) == kinds:
            if r - l < diff:
                answer = [l + 1, r]
                diff = r - l

            if d[gems[l]] == 1:
                del d[gems[l]]
            else:
                d[gems[l]] -= 1
            l += 1

        # 보석의 종류 개수와 같지 않을 경우
        elif len(d) != kinds:
            if r >= n:
                break
            if gems[r] in d:
                d[gems[r]] += 1
            else:
                d[gems[r]] = 1
            r += 1
    return answer