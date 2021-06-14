import sys

def search(index):
    minval = sys.maxsize
    ans = -1
    flag = False
    for i in range(index + 1, n):
        if not visited[i]:
            if ord(word[i]) - ord('A') < minval:
                flag = True
                minval = ord(word[i]) - ord('A')
                ans = i

    if flag:
        visited[ans] = True
        stack.append(ans)
        return ans
    else:
        return -1

def print_word():
    ans = ""
    for i in range(n):
        if visited[i]:
           ans += word[i]
    print(ans)

word = input()
n = len(word)
visited = [False] * n
stack = []

while True:
    if all(visited):
        break

    if not stack:
        if search(-1) != -1:
            print_word()
    else:
        flag = False
        while not flag:
            if not stack:
                if search(-1) != -1:
                    flag = True
                    print_word()
                else:
                    break
            else:
                idx = stack[-1]
                if search(idx) != -1:
                    flag = True
                    print_word()
                else:
                    stack.pop()

