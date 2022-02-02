from itertools import permutations
import copy
import sys


def solution(expression):
    # 숫자와 연산자 구분
    nums = []
    opers = []
    num = ""
    for exp in expression:
        if exp not in "+*-":
            num += exp
        else:
            nums.append(int(num))
            opers.append(exp)
            num = ""
    nums.append(int(num))  # 마지막 숫자 append

    cases = list(permutations(set(opers), len(set(opers))))
    answer = -sys.maxsize
    for case in cases:
        newnums = copy.deepcopy(nums)
        newoper = copy.deepcopy(opers)
        for c in case:
            while True:
                try:
                    idx = newoper.index(c)
                except:
                    break
                if c == "+":
                    newnums[idx] = newnums[idx] + newnums[idx + 1]
                    del newnums[idx + 1]
                    del newoper[idx]
                elif c == "-":
                    newnums[idx] = newnums[idx] - newnums[idx + 1]
                    del newnums[idx + 1]
                    del newoper[idx]
                elif c == "*":
                    newnums[idx] = newnums[idx] * newnums[idx + 1]
                    del newnums[idx + 1]
                    del newoper[idx]

        answer = max(answer, abs(newnums[0]))
    return answer