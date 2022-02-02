n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
answer = 0

for i in range(n-2):
    start, end = i+1, n-1
    while start < end:
        if cards[i] + cards[start] + cards[end] <= m:
            answer = max(answer, cards[i] + cards[start] + cards[end])
            start += 1
        else:
            end -= 1
print(answer)
