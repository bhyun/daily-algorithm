from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))


cases = list(combinations(range(n), n//2))
answer = sys.maxsize
for case in cases:
    team1 = set(case)
    team2 = set(range(n)) - team1
    s1, s2 = 0, 0
    for i in team1:
        for j in team1:
            if i != j:
                s1 += s[i][j]
    for i in team2:
        for j in team2:
            if i != j:
                s2 += s[i][j]
    answer = min(answer, abs(s1 - s2))

print(answer)

