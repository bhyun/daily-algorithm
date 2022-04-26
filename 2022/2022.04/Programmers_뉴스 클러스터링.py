import re
from collections import defaultdict


def solution(str1, str2):
    mapper1 = defaultdict(int)
    mapper2 = defaultdict(int)

    pattern = re.compile('[a-zA-Z]+')
    for i in range(len(str1) - 1):
        string = str1[i:i + 2]
        if re.fullmatch(pattern, string):
            mapper1[string.lower()] += 1

    for i in range(len(str2) - 1):
        string = str2[i:i + 2]
        if re.fullmatch(pattern, string):
            mapper2[string.lower()] += 1

    keys = set(mapper1.keys()).union(set(mapper2.keys()))

    intersection = 0
    union = 0

    for key in keys:
        if mapper1[key] and mapper2[key]:
            intersection += min(mapper1[key], mapper2[key])
            union += max(mapper1[key], mapper2[key])
        else:
            union += max(mapper1[key], mapper2[key])

    if intersection == 0 and union == 0:
        return 65536

    return int(65536 * intersection / union)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))