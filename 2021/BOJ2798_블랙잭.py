n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
answer = 0
for i in range(n-2):
    summary = card[i]
    left, right = i+1, n-1
    while left < right:
        if summary + card[left] + card[right] > m:
            right -= 1
        elif summary + card[left] + card[right] <= m:
            if summary + card[left] + card[right] > answer:
                answer = summary + card[left] + card[right]
            left += 1
print(answer)