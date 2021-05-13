from collections import deque

def bfs(number):
    q = deque([number])
    while q:
        num = q.popleft()
        standard = num
        while standard != 0:
            num += (standard % 10)
            standard //= 10
        # 범위 내에 있고, 셀프넘버 후보가 될 수 있으면
        if num <= 10000 and selfNumber[num]:
            selfNumber[num] = False
            q.append(num)
        else:
            return


selfNumber = [True]*(10001)
for i in range(1, 10001):
    bfs(i)
for i in range(1, 10001):
    if selfNumber[i]:
        print(i)