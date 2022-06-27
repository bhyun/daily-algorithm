import sys

def calculate(num1, num2, oper):
    if oper == "+":
        return num1 + num2
    if oper == "-":
        return num1 - num2
    else:
        return num1 * num2

def dfs(result, index):
    global answer

    if index == n - 1:
        answer = max(answer, result)
        return

    if index + 2 < n:
        dfs(calculate(result, int(string[index+2]), string[index+1]), index + 2)
    if index + 4 < n:
        dfs(calculate(result, calculate(int(string[index + 2]), int(string[index + 4]), string[index + 3]), string[index + 1]), index + 4)

answer = -sys.maxsize
n = int(input())
string = input()
dfs(int(string[0]), 0)
if n > 2:
    dfs(calculate(int(string[0]), int(string[2]), string[1]), 2)
print(answer)
