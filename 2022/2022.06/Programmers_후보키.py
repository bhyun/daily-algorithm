from collections import deque

answer = []

def enable_candidate_key(relation, key):

    temp = set()
    for i in range(len(relation)):
        tmp = ""
        for j in range(len(key)):
            tmp += relation[i][key[j]]
        temp.add(tmp)

    # 유일성 체크
    if len(temp) != len(relation):
        return False

    # 최소성 체크
    for ans in answer:
        if ans.issubset(key):
            return False
    return True

def solution(relation):
    global answer

    m = len(relation[0])

    q = deque()
    for i in range(m):
        q.append(([i], i))

    while q:
        key, index = q.popleft()

        # 후보키가 될 수 있는지 파악한다.
        if enable_candidate_key(relation, key):
            answer.append(set(key))
            continue

        for i in range(index + 1, m):
            next_key = key + [i]
            q.append((next_key, i))

    return len(answer)