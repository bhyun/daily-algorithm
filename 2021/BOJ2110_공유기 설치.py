def setting(itv):
    cnt = 1
    last = home[0]
    for i in range(1, n):
        if home[i] >= last + itv:
            cnt += 1
            last = home[i]
    return cnt

n, c = map(int, input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()

start, end = 1, home[-1] - home[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = setting(mid)
    if cnt >= c:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)