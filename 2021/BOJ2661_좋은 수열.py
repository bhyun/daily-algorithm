import sys
input = sys.stdin.readline

def check(num):
    length = len(num)
    for i in range(1, length//2+1):
        if num[-i:] == num[-2*i:-i]:
            return False
    return True

def dfs(num):

    if len(num) == n:
        print(num)
        exit()

    for i in range(1, 4):
        if num and num[-1] == str(i):
            continue
        if check(num + str(i)):
            dfs(num + str(i))
n = int(input())
dfs("")
