import sys
input = sys.stdin.readline

def dfs(summary, i, cnt):
    global minval, maxval
    if cnt == op_cnt:
        if summary < minval:
            minval = summary
        if summary > maxval:
            maxval = summary

    # summary 계산하기
    for j in range(op_cnt):
        if not opV[j]:
            opV[j] = True
            if op[j] == "+":
                dfs(summary + arr[i], i+1, cnt+1)
            elif op[j] == "-":
                dfs(summary - arr[i], i+1, cnt+1)
            elif op[j] == "*":
                dfs(summary * arr[i], i+1, cnt+1)
            else:
                if summary < 0:
                    dfs(-((-summary) // arr[i]), i+1, cnt+1)
                else:
                    dfs(summary//arr[i], i+1, cnt+1)
            opV[j] = False


n = int(input())
arr = list(map(int, input().split()))
data = list(map(int, input().split()))
op_cnt = sum(data)
op = ["+"] * data[0] + ["-"] * data[1] + ["*"] * data[2] + ["/"] * data[3]
minval = sys.maxsize
maxval = -sys.maxsize

opV = [False] * op_cnt

# 첫 시작하기
dfs(arr[0], 1, 0)

print(maxval)
print(minval)
