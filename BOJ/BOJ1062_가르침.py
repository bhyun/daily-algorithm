def check():
    cnt = 0
    for word in words:
        for w in word:
            if not visited[ord(w) - ord('a')]:
                break
        else:
            cnt += 1
    return cnt


def dfs(index, k):
    global answer
    if k == 0:
        cnt = check()
        answer = max(answer, cnt)
        return

    for i in range(index + 1, 26):
        if not visited[i]:
            visited[i] = True
            dfs(i, k - 1)
            visited[i] = False


n, k = map(int, input().split())
words = []
for _ in range(n):
    words.append(set(input()))

visited = [False] * 26
visited[ord('a')-ord('a')] = True
visited[ord('n')-ord('a')] = True
visited[ord('t')-ord('a')] = True
visited[ord('i')-ord('a')] = True
visited[ord('c')-ord('a')] = True

if k < 5:
    print(0)
else:
    answer = 0
    k -= 5
    dfs(0, k)
    print(answer)

