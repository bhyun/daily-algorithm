def split(word):
    cnt = 0
    for i, w in enumerate(word):
        if w == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return word[:i + 1], word[i + 1:]


def isright(word):
    cnt = 0
    for w in word:
        if w == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
    return True


def solution(p):
    if p == "":
        return ""
    u, v = split(p)
    if isright(u):  # 올바른 문자열
        return u + solution(v)
    else:  # 균형잡힌 문자열
        string = "("
        string += solution(v)
        string += ")"
        for s in u[1:-1]:
            if s == "(":
                string += ")"
            else:
                string += "("
        return string
