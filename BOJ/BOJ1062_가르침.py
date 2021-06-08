def check(realwords, char):
    cnt = 0
    for realword in realwords:
        for w in realword:
            if char[ord(w)-ord('a')] != 1:
                break
        else:
            cnt += 1
    return cnt


def dfs(index, count):
    global answer

    if count == k-5:
        # 단어 체크
        cnt = check(realwords, char)
        answer = max(answer, cnt)

    else:
        for i in range(index, len(cand)):
            if char[ord(cand[i])-ord('a')] != 1:
                char[ord(cand[i])-ord('a')] = 1
                dfs(i+1, count + 1)
                char[ord(cand[i])-ord('a')] = 0


n, k = map(int, input().split())
char = [0] * 26
words = []
for _ in range(n):
    words.append(input())

# 예외
if k < 5:
    print(0)

else:
    # 배운 단어
    char[ord('a')-ord('a')] = 1
    char[ord('n') - ord('a')] = 1
    char[ord('t') - ord('a')] = 1
    char[ord('i') - ord('a')] = 1
    char[ord('c') - ord('a')] = 1
    # antic 제외한 단어
    realwords = []
    # antic 제외한 문자
    cand = set()

    for word in words:
        realwords.append(word[4:-4])
        for w in word[4:-4]:
            if char[ord(w) - ord('a')] != 1:
                cand.add(w)
    cand = list(cand)

    # 예외 - 배울 수 있는 단어가 더 많으면 모든 단어 배울 수 있음.
    if len(cand) <= k-5:
        print(n)

    else:
        answer = 0
        dfs(0, 0)
        print(answer)

