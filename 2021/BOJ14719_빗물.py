h, w = map(int, input().split())
heights = list(map(int, input().split()))

stack = []
now = []
rain = 0

for height in heights:
    if not stack:
        stack.append(height)
    elif stack[-1] <= height:
        val = stack.pop()
        stack.append(height)
        while now:
            rain += val - now.pop()

    else:

        for i, n in enumerate(now):
            if now[i] < height:
                rain += height - now[i]
                now[i] += (height - now[i])
        now.append(height)

print(rain)