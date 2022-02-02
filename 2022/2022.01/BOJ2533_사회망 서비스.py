import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def solve(cur):
    # 현재 방문하는 노드를 방문처리해준다.
    visited[cur] = True

    # 현재 방문하는 노드와 연결된 노드를 방문한다.
    for neighbor in tree[cur]:
        # 방문하지 않은 경우에만 탐색한다.
        if not visited[neighbor]:
            solve(neighbor) # 가장 하단인 리프노드까지 방문한다.

            # 내가 ea이지 않은 경우에는 연결된 모든 친구들이 ea여야한다.
            dp[cur][0] += dp[neighbor][1]

            # 내가 ea인 경우에는 연결된 친구들이 ea여도 되고 ea가 아니여도 된다. 둘 중 작은 값을 선택한다.
            dp[cur][1] += min(dp[neighbor][0], dp[neighbor][1])

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n+1)
dp = [[0, 1] for _ in range(n+1)] # 내가 ea인경우 ea의 수, 내가 ea가 아닌 경우 ea의 수
solve(1)

print(min(dp[1][0], dp[1][1]))