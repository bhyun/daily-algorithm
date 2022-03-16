# 다시풀기
import re
from collections import deque
from itertools import permutations
from copy import deepcopy

def calculate(oper, a, b):
    if oper == "+":
        return a + b
    elif oper == "*":
        return a * b
    else:
        return a - b

def solution(expression):
    answer = 0

    origin_opers = deque(re.findall('[-+*]', expression))
    origin_nums = deque(map(int, re.findall('[0-9]+', expression)))

    set_opers = set(origin_opers)
    cases = list(permutations(set_opers, len(set_opers)))


    for case in cases:
        nums = deepcopy(origin_nums)
        opers = deepcopy(origin_opers)
        for c in case:
            temp_oper = deque()
            temp_nums = deque()
            for oper in opers:
                if oper == c:
                    nums.appendleft(calculate(oper, nums.popleft(), nums.popleft()))
                else:
                    temp_nums.append(nums.popleft())
                    temp_oper.append(oper)

            while nums:
                temp_nums.append(nums.popleft())

            nums = temp_nums
            opers = temp_oper

        answer = max(answer, abs(nums.popleft()))

    return answer


print(solution("100-200*300-500+20"))