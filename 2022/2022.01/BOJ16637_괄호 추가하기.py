import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def calculate(num1, num2, oper):
    if oper == "+":
        return num1 + num2
    elif oper == "*":
        return num1 * num2
    else:
        return num1 - num2

def dfs(index, result):
    global answer

    if index > n - 1:
        answer = max(answer, result)
        return

    oper = nums[index]
    # 괄호 추가하는 경우
    if index + 3 < n:
        num1, num2, inter = nums[index+1], nums[index+3], nums[index+2]
        temp = calculate(result, calculate(num1, num2, inter), oper)
        dfs(index + 4, temp)

    # 괄호 추가하지 않는 경우
    if index + 1 < n:
        num3 = nums[index+1]
        temp = calculate(result, num3, oper)
        dfs(index + 2, temp)

n = int(input())
nums = list(input())
for i in range(n):
    if i % 2 == 0:
        nums[i] = int(nums[i])
if n == 1:
    print(nums[0])
else:
    answer = -sys.maxsize
    temp = calculate(nums[0], nums[2], nums[1])
    dfs(3, temp)
    dfs(1, nums[0])
    print(answer)
