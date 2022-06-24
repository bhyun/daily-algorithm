from collections import defaultdict

def solution(gems):
    answer = []
    start = 0

    target = len(set(gems))
    mapper = defaultdict(int)
    cur = 0
    for end in range(len(gems)):

        gem = gems[end]
        mapper[gem] += 1
        cur += (mapper[gem] == 1)

        if cur == target:
            # 시작지점 이동하기
            s_gem = gems[start]
            while start < end and mapper[s_gem] > 1:
                mapper[s_gem] -= 1
                start += 1
                s_gem = gems[start]

            # 최소 구간 갱신하기
            if not answer or end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]
                mapper[gems[start]] -= 1
                cur -= 1
                start += 1

    return answer