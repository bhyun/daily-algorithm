import math
from itertools import permutations


def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    n = len(numbers)
    answer = set()
    for i in range(1, n + 1):
        nums = set(permutations(numbers, i))
        for num in nums:
            new = int("".join(num))
            if isPrime(new):
                answer.add(new)
    return len(answer)