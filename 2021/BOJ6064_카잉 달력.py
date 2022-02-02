import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    flag = False
    while x <= m * n:

        if x % n == y % n:
            flag = True
            print(x)
            break

        x += m

    if not flag:
        print(-1)




