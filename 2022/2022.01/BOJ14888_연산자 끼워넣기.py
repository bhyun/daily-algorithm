import sys
input = sys.stdin.readline

def operate(first, second, oper):
    if oper == "+":
        return first + second
    elif oper == "-":
        return first - second
    elif oper == "*":
        return first * second
    else:
        if first < 0:
            return -(abs(first) // second)
        else:
            return first // second

def solve(cal, index, add, substract, multiply, divide):
    global minAns, maxAns
    if index == n:
        minAns = min(minAns, cal)
        maxAns = max(maxAns, cal)
        return

    if add > 0:
        solve(cal + nums[index], index + 1, add - 1, substract, multiply, divide)
    if substract > 0:
        solve(cal - nums[index], index + 1, add, substract - 1, multiply, divide)
    if multiply > 0:
        solve(cal * nums[index], index + 1, add, substract, multiply - 1, divide)
    if divide > 0:
        solve(int(cal / nums[index]), index + 1, add, substract, multiply, divide - 1)

n = int(input())
nums = list(map(int, input().split()))
add, substract, multiply, divide = map(int, input().split())
minAns, maxAns = sys.maxsize, -sys.maxsize
solve(nums[0], 1, add, substract, multiply, divide)
print(maxAns)
print(minAns)