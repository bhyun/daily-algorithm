n = int(input())
tot = int(input())
recommend = list(map(int, input().split()))
cnt = {}
order = []
for i, r in enumerate(recommend):
    # 추천 번호가 이미 게시되어 있는 상태
    if r in cnt:
        cnt[r] += 1
    else:
        # 사진이 꽉찼을 경우
        if len(order) >= n:
            minval = min(cnt.values())
            temp = []
            for k, v in cnt.items():
                if v == minval:
                    if not temp:
                        temp.append(k)
                    elif order.index(temp[-1]) > order.index(k):
                        temp.pop()
                        temp.append(k)
            order.remove(temp[0])
            del cnt[temp[0]]
        cnt[r] = 1
        order.append(r)
answer = []
for k, v in cnt.items():
    answer.append(k)
answer.sort()
print(*answer)