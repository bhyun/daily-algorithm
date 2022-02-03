import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    answer = 0
    while len(cards) >= 2:
        c1 = heapq.heappop(cards)
        c2 = heapq.heappop(cards)
        answer += c1 + c2
        heapq.heappush(cards, c1 + c2)
    print(answer)