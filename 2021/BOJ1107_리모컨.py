from bisect import bisect_left

n = input() # target
m = int(input())
normal = list(set(range(10)) - set(map(int, input().split()))) # 정상 버튼
# 숫자 버튼 -> +, - 버튼
temp = ""
for i in n:
    i = int(i)
    if i not in normal:
        # normal인 수 중에서 가장 가까운 수
        a = bisect_left(normal, i)
        if a == len(normal):
            temp += str(normal[a-1])
        elif a == 0:
            temp += str(normal[a])
        else:
            if abs(normal[a-1]-i) <= abs(normal[a-i]):
                temp += str(normal[a-1])
            else:
                temp += str(normal[a])
    else:
        temp += str(i)

if len(temp) + abs(int(temp) - int(n)) <= abs(int(n)-100):
    print(len(temp) + abs(int(temp) - int(n)))
else:
    print(abs(int(n)-100))


