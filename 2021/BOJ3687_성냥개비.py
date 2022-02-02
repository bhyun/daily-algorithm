import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    maxval = [-sys.maxsize] * (101)
    minval = [sys.maxsize] * (101)
    nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    # 초기화
    for i,num in enumerate(nums):
        if maxval[num] < num:
            maxval[num] = i
        if minval[num] > num:
            minval[num] = i

    # 성냥개비 개수
    for i in range(2, n+1):
        for j in range(1, i):
            if minval[j] != sys.maxsize and minval[i-j] != sys.maxsize:
                if j == 6:
                    minimum = str(6) + str(minval[i-j])
                else:
                    minimum = str(minval[j]) + str(minval[i-j])
                if int(minimum) < minval[i]:
                    minval[i] = int(minimum)
            if maxval[j] != -sys.maxsize and maxval[i-j] != -sys.maxsize:
                maximum = str(maxval[j]) + str(maxval[i-j])
                if int(maximum) > maxval[i]:
                    maxval[i] = int(maximum)
    if n == 6:
        print(6, maxval[n])
    else:
        print(minval[n], maxval[n])
