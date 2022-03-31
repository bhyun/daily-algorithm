import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))

bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()

able_to_carry = []
answer = 0
for bag in bags:
    
    while jewels and jewels[0][0] <= bag:
        m, v = heapq.heappop(jewels)
        heapq.heappush(able_to_carry, -v)

    if able_to_carry:
        answer -= heapq.heappop(able_to_carry)
    elif not jewels:
        break

print(answer)