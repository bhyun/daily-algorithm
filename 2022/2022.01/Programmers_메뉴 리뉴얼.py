from itertools import combinations

def check(dic):
    result = set()
    value = 0
    for (k, v) in dic.items():
        if v >= 2:
            if v == value:
                result.add("".join(k))
            elif v > value:
                value = v
                result = set()
                result.add("".join(k))
    return result

def solution(orders, course):
    answer = []

    for i, order in enumerate(orders):
        order = "".join(sorted(order))
        orders[i] = order

    for i in course:
        dic = {}
        for order in orders:
            cases = list(combinations(order, i))
            for case in cases:
                if case not in dic:
                    dic[case] = 1
                else:
                    dic[case] += 1

        result = list(check(dic))
        for rs in result:
            answer.append(rs)
    answer.sort()
    return answer