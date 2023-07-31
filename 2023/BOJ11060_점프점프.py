import sys
from collections import deque
input = sys.stdin.readline

# input
n = int(input())
miro = list(map(int, input().split()))
visited = [False] * (n+1)
answer = sys.maxsize

# 예외 처리
if n == 0:
    print(-1)
elif n == 1:
    print(0)
else:
    answer = sys.maxsize

    # enqueue
    q = deque()
    for i in range(0, miro[0] + 1):
        if i <= n - 1:
            visited[i] = True
            q.append((i, 0))  # 현재 위치, 점프 횟수

    # 완전 탐색
    while q:
        idx, jump_cnt = q.popleft()

        # 종료조건
        if idx == n - 1:
            answer = min(answer, jump_cnt + 1)
            continue

        # 백트래킹
        if jump_cnt > answer:
            continue

        for i in range(idx, idx + miro[idx] + 1):
            if i <= n - 1 and not visited[i]:
                if miro[i] == 0:
                    continue
                visited[i] = True
                q.append((i, jump_cnt + 1))

    if answer == sys.maxsize:
        print(-1)
    else:
        print(answer)