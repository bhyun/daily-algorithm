from collections import Counter

n = int(input())
answer = 0
for _ in range(n):
    word = input()
    d = Counter(word)
    stack = []
    for w in word:
        if not stack:
            stack.append(w)
            d[w] -= 1
        elif stack[-1] != w:
            s = stack.pop()
            if d[s] != 0:
                break
            stack.append(w)
            d[w] -= 1
        else:
            d[w] -= 1
    else:
        answer += 1
print(answer)

