def solution(arr):
    def divide(start_x, start_y, length):
        nonlocal zeros, ones
        standard = arr[start_x][start_y]
        for i in range(start_x, start_x + length):
            for j in range(start_y, start_y + length):
                if arr[i][j] != standard:
                    divide(start_x, start_y, length // 2)
                    divide(start_x, start_y + length // 2, length // 2)
                    divide(start_x + length // 2, start_y, length // 2)
                    divide(start_x + length // 2, start_y + length // 2, length // 2)
                    return
        if standard == 0:
            zeros += 1
        elif standard == 1:
            ones += 1

    zeros = 0
    ones = 0
    n = len(arr)
    divide(0, 0, n)
    return [zeros, ones]