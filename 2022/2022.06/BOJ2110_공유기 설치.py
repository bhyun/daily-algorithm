import sys
input = sys.stdin.readline

def install(dist, target):
    last = house[0]
    cnt = 1
    for i in range(1, n):
        if house[i] - last >= dist:
            cnt += 1
            last = house[i]

    if cnt >= target:
        return True
    return False


n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
start, end = 0, house[-1] - house[0]
answer = 0
while start <= end:
    mid = (start + end) // 2

    if install(mid, c):
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)


