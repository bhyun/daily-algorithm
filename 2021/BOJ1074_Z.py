n, r, c = map(int, input().split())

def divide(x, y, length, num):
    if length > 2:
        if x <= r < x + length // 2 and y <= c < y + length // 2:
            divide(x, y, length//2, num)
        elif x <= r < x + length // 2 and y + length // 2 <= c < y + length:
            divide(x, y + length // 2, length//2, num + (length // 2) ** 2)
        elif x + length // 2 <= r < x + length and y <= c < y + length // 2:
            divide(x + length // 2, y, length//2, num + (2 * (length // 2) ** 2))
        elif x + length // 2 <= r < x + length and y + length // 2 <= c < y + length:
            divide(x + length // 2, y + length // 2 , length//2, num + (3 * (length // 2) ** 2))
        return

    elif length == 2:
        if x == r and y == c:
            print(num)
        elif x == r and y + 1 == c:
            print(num + 1)
        elif x + 1 == r and y == c:
            print(num + 2)
        elif x + 1 == r and y + 1 == c:
            print(num + 3)
        return

divide(0, 0, 2 ** n , 0)