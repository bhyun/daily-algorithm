import heapq
import sys
input = sys.stdin.readline

n = int(input())
lesson = []
for _ in range(n):
    lesson.append(list(map(int, input().split())))
lesson.sort(key=lambda x:x[0])
q = []
heapq.heappush(q, lesson[0][1]) # 끝나는 시간 기록

for i in range(1, n):
    if lesson[i][0] >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, lesson[i][1])
    else:
        heapq.heappush(q, lesson[i][1])

print(len(q))