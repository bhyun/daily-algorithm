def calculate(num, p):
    answer = 0
    while num != 0:
        answer += (num % 10)** p
        num //= 10
    return answer

a, p = map(int, input().split())
stack = [a]
idx = 0
flag = True
while True:
    val = calculate(a, p)
    for i, s in enumerate(stack):
        if s == val:
            idx = i
            flag = False
            break
    a = val
    stack.append(a)
    if not flag:
        break
print(len(stack[:idx]))