import copy
import re
from itertools import permutations


def calculate(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    else:
        return num1 * num2

def solution(expression):
    nums = list(map(int, re.findall('\d+', expression)))
    operator = re.findall('[-+*]', expression)

    cases = list(permutations(set(operator), len(set(operator))))
    answer = []
    for case in cases:

        cnums = copy.deepcopy(nums)
        coper = copy.deepcopy(operator)
        for c in case:
            while c in coper:
                idx = coper.index(c)
                result = calculate(c, cnums[idx], cnums[idx + 1])
                cnums[idx] = result
                del coper[idx]
                del cnums[idx + 1]
        answer.append(abs(cnums[0]))
    return max(answer)


print(solution("100-200*300-500+20"))

