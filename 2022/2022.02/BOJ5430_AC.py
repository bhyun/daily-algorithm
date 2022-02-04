import re
from collections import deque

def search(p, nums):
    start, end = 0, len(nums) - 1
    cur = start
    cnt = 0
    for i in p:
        if i == "R":
            cur = end if cur == start else start
            cnt += 1
        else:
            if not nums:
                return False, []
            if cur == start:
                nums.popleft()
            elif cur == end:
                nums.pop()
    if cnt % 2:
        nums.reverse()
    return True, nums

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    nums = deque(re.findall("[0-9]+", input()))
    is_correct, result = search(p, nums)
    if is_correct:
        answer = "["
        answer += ",".join(nums)
        answer += "]"
    else:
        answer = "error"
    print(answer)
