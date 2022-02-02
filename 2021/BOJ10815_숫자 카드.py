import sys
input = sys.stdin.readline

def binarySearch(target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if given[mid] == target:
            return True

        if given[mid] > target:
            right = mid - 1
        elif given[mid] < target:
            left = mid + 1
    return False


n = int(input())
given = list(map(int, input().split()))
given.sort()

m = int(input())
cards = list(map(int, input().split()))

for card in cards:
    if binarySearch(card):
        print(1, end=" ")
    else:
        print(0, end=" ")