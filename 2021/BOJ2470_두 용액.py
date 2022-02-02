import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
left, right = 0, n-1
diff = sys.maxsize
answer = []
while left < right:
    summary = solutions[left] + solutions[right]
    if abs(summary) < diff:
        diff = abs(summary)
        answer = [solutions[left], solutions[right]]

    if summary >= 0:
        right -= 1
    elif summary < 0:
        left += 1
print(*answer)
