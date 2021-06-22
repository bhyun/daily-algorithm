from collections import deque
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

q = deque(permutations(arr, n))
answer = 0
while q:
    seq = q.popleft()
    summary = 0
    for i in range(n-1):
        summary += abs(seq[i] - seq[i+1])
    if summary > answer:
        answer = summary
print(answer)