def install(dist):
    cnt = 1
    idx = 0
    for i in range(1, n):
        if homes[i] - homes[idx] >= dist:
            idx = i
            cnt += 1
    return cnt

n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]

homes.sort()
start, end = 0, homes[-1] - homes[0]
answer = 0
while start <= end:
    mid = (start + end) // 2 # 간격
    cnt = install(mid)
    if cnt >= c:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)

