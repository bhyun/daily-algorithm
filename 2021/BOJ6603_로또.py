import sys
from collections import deque
input = sys.stdin.readline

while True:
    data = input()
    if data[0] == '0':
        break
    ls = list(map(int, data.split()))
    k, s = ls[0], ls[1:]
    q = deque()
    for i in range(k-5):
        q.append(([s[i]], i))

    while q:
        nums, idx = q.popleft()
        if len(nums) == 6:
            print(*nums)
            continue

        for i in range(idx+1, k):
            q.append((nums + [s[i]], i))
    print()