from collections import deque

def check(b_id, u_id):
    if len(b_id) != len(u_id):
        return False
    for b, u in zip(b_id, u_id):
        if b != "*":
            if b != u:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    q = deque()
    # 시작 위치 찾기
    for u_id in user_id:
        if check(banned_id[0], u_id):
            q.append(([u_id], 0))
    while q:
        path, idx = q.popleft()
        if len(path) == len(banned_id):
            path.sort()
            if path not in answer:
                answer.append(path)
            continue

        for u_id in user_id:
            if check(banned_id[idx + 1], u_id):
                if u_id not in path:
                    q.append((path + [u_id], idx + 1))

    return len(answer)