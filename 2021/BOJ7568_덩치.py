n = int(input())
physical = []
for _ in range(n):
    h, w = map(int, input().split())
    physical.append((h, w))
answer = []
for i in range(n):
    rank = 1
    h1, w1 = physical[i]
    for j in range(n):
        h2, w2 = physical[j]
        if h1 < h2 and w1 < w2:
            rank += 1
    answer.append(rank)

print(*answer)
