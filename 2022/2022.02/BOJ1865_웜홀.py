import sys
input = sys.stdin.readline

def search():
    distance = [sys.maxsize] * (n + 1)
    for i in range(n):
        for a, b, c in edges:
            if distance[b] > distance[a] + c:
                distance[b] = distance[a] + c

                if i == n-1:
                    return False
    return True

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())

    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))

    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    if not search():
        print("YES")
    else:
        print("NO")
