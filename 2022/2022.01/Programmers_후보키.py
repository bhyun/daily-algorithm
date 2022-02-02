from itertools import combinations

def solution(relation):
    answer = 0

    n = len(relation)
    m = len(relation[0])
    candidates = list(range(m))
    check = [False] * m

    for i in range(1, m + 1):
        cases = list(combinations(candidates, i))
        for case in cases:
            # 후보키가 될 수 있는지 체크
            for c in case:
                if check[c]:
                    break
            else:
                # 후보키 가능 후보
                tempValue = []
                for j in range(n):
                    tmp = []
                    for c in case:
                        tmp.append(relation[j][c])
                    if tmp in tempValue:
                        break
                    tempValue.append(tmp)
                else:
                    for c in case:
                        check[c] = True
                    answer += 1

    return answer
