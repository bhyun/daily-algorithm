#PyPy3로 제출했을 때 통과
from collections import deque

def isPrime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
           return False
    return True

n = int(input())
q = deque([2, 3, 5, 7])

length = 1
while q:
    num = q.popleft()

    if len(str(num)) == n:
        print(num)
        continue

    for i in range(1, 10, 2):
        new = int(str(num) + str(i))
        if isPrime(new):
            q.append(new)

