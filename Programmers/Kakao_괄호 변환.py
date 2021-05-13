def check(p):
    cnt = 0
    for i in p:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return 0 # 균형잡힌 문자열
    return 1 # 올바른 문자열

def divide(p):
    cnt = 0
    u = ""
    for i, s in enumerate(p):
        if s == "(":
            u += s
            cnt += 1
        if s == ")":
            cnt -= 1
            u += s
        if cnt == 0:
            break
    return u, p[i+1:] # 균형, 올바른

def solution(p):
    if p == "":
        return ""

    u, v = divide(p)
    if check(u): # u가 올바른 문자열이면
        ans = u
        ans += solution(v)
        return ans
    else: # u가 균형잡힌 문자열
        ans = "("
        ans += solution(v)
        ans += ")"
        for i in u[1:-1]:
            if i == '(':
                ans += ')'
            else:
                ans += '('
        return ans