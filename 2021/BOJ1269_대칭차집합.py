### 이진 탐색을 사용한 문제 풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
answer = []

# Binary Search
def binarySearch(target, array):
    left, right = 0, len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        elif array[mid] == target:
            return True

    return False


# A-B
for i in a:
    if not binarySearch(i, b):
        answer.append(i)

# B-A
for i in b:
    if not binarySearch(i, a):
        answer.append(i)
print(len(answer))


### 파이썬 set 연산을 활용한 문제 풀이
n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a - b) + len(b - a))