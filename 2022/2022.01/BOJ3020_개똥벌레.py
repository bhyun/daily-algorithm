import sys

def binarySearch(target, array):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return len(array) - start

n, h = map(int, input().split())
top = [] # 종유석
bottom = [] # 석순
for i in range(n):
    if i % 2 == 0:
        bottom.append(int(input()))
    else:
        top.append(int(input()))

top.sort()
bottom.sort()

result, cnt = sys.maxsize, 0
for i in range(1, h+1):
    curCnt = binarySearch(i, top) + binarySearch(h - i + 1, bottom) # 종유석 + 석순
    if curCnt < result:
        result = curCnt
        cnt = 1
    elif curCnt == result:
        cnt += 1

print(result, cnt)


