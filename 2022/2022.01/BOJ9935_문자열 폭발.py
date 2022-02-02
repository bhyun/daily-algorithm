string = input()
bomb = input()

stack = []
for s in string:
    stack.append(s)
    if len(stack) >= len(bomb) and s == bomb[-1]:
        if "".join(stack[-len(bomb):]) == bomb:
            for i in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")