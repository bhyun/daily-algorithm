from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []

    profit = defaultdict(int)
    parent = defaultdict(str)

    for e, r in zip(enroll, referral):
        if r == "-":
            continue
        parent[e] = r

    for s, a in zip(seller, amount):

        cur = s
        amt = a * 100

        while True:

            if not parent[cur]:
                profit[cur] += amt - int(amt * 0.1)
                break

            if amt * 0.1 < 1:
                profit[cur] += amt
                break

            na = int(amt * 0.1)
            profit[cur] += amt - na
            amt = na
            cur = parent[cur]

    for e in enroll:
        answer.append(profit[e])

    return answer