def solution(l, s, n):
    # s 정렬
    s.sort()

    if n in s:
        return 0

    # start, end 초기값 설정
    start = 1
    end = s[-1] - 1

    # start, end 위치찾기
    for idx, val in enumerate(s):
        if val < n:
            start = val + 1
        else:
            end = val - 1
            break
    return (n - start + 1) * (end - n + 1) - 1


if __name__ == "__main__":
    l = int(input())
    s = list(map(int, input().split()))
    n = int(input())
    print(solution(l, s, n))
