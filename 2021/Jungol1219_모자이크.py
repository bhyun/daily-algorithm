def check(length, paper):
    start = wrongs[0][1]   # 가장 왼쪽에 있는 열
    for i in range(1, n):
        if wrongs[i][1] > start + length - 1:
            start = wrongs[i][1]
            paper -= 1
            if paper == 0:
                return False
    else:
        return True


r, c = map(int, input().split())
paper = int(input())
n = int(input())
wrongs = []
minLength, maxLength = -1, 1000000
for _ in range(n):
    x, y = map(int, input().split())
    if x > minLength:
        minLength = x
    wrongs.append((x, y))

wrongs.sort(key=lambda x: x[1])

while minLength <= maxLength:
    length = (minLength + maxLength) // 2
    if check(length, paper):
        maxLength = length - 1
    else:
        minLength = length + 1

print(minLength)