# 에라토스테네스의 체
prime = [True] * 4000001
prime[0], prime[1] = False, False
for i in range(2, 4000001//2):
    for j in range(2*i, 4000001, i):
        prime[j] = False

n = int(input())
prime_list = list(filter(lambda x: prime[x], list(range(n+1))))

answer = 0
start, end = 0, 0
while end < len(prime_list):
    summary = sum(prime_list[start: end + 1])

    if summary == n:
        answer += 1
        end += 1
    elif summary < n:
        end += 1
    elif summary > n:
        start += 1

print(answer)