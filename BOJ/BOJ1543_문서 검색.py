### 나의 풀이
# for i in range(n-m+1)에서 range(n-m)이라고 설정해서 틀림 -> range(n-m+1)로 수정하여 통과
# 문자열의 크기가 크지않아 완전탐색으로 문제해결

data = input()
target = input()
n = len(data)
m = len(target)
answer = 0

for i in range(n-m+1):
    idx = i
    cnt = 0
    if data[idx:idx+m] != target:
        continue
    while idx < n:
        if data[idx:idx + m] == target:
            idx += m
            cnt += 1
        else:
            idx += 1
    answer = max(answer, cnt)
print(answer)


### 다른사람 풀이
# 나는 시작 위치를 변경해가면서 문제를 풀었는데, 다른사람은 시작위치는 맨처음으로 고정한다음에 문자열을 한번만 탐색하였다.


data = input()
target = input()
n = len(data)
m = len(target)
i = 0
count = 0
while i <= n - m:
    if data[i:i+m] == target:
        count += 1
        i += m
    else:
        i += 1
print(count)