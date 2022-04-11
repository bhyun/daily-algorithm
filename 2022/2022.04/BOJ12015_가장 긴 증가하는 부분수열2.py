import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

temp = [nums[0]]
for i in range(1, n):

    if nums[i] > temp[-1]:
        temp.append(nums[i])
    else:
        start, end = 0, len(temp) - 1
        while start <= end:
            mid = (start + end) // 2

            if temp[mid] >= nums[i]:
                end = mid - 1
            else:
                start = mid + 1

        if start < len(temp):
            temp[start] = nums[i]

print(len(temp))


