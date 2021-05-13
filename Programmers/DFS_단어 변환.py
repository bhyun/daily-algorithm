import sys


def solution(begin, target, words):
    n = len(begin)
    m = len(words)
    answer = sys.maxsize

    # target 단어가 있는지 확인하기
    if target not in words:
        return 0

    def checkWord(before, word):
        diff = 0
        for i in range(n):
            if before[i] != word[i]:
                diff += 1
                if diff > 1:
                    return False
        if diff == 0:
            return False
        return True

    def dfs(word, path):
        nonlocal answer
        if word == target:
            answer = min(answer, len(path))
            return

        for i in range(m):
            if not visited[i] and checkWord(word, words[i]):
                visited[i] = True
                dfs(words[i], path + [words[i]])
                visited[i] = False

    for i, word in enumerate(words):
        visited = [False] * m
        if checkWord(begin, word):
            print(word)
            visited[i] = True
            dfs(word, [word])
    return answer