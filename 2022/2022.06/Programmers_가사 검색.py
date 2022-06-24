# 정확성 통과
# 효율성 1, 3번 통과 못함
#### bisect로 풀어도 되지만, 트라이 알고리즘 학습 후 재도전?

def binary_search(words, target):
    start, end = 0, len(words) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > words[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return start

def count_match_word(words, index, target):
    cnt = 0
    for i in range(index, len(words)):
        if words[i] <= target:
            cnt += 1
        else:
            return cnt
    return cnt

def solution(words, queries):
    answer = []

    origin_mapper = [[] for _ in range(10001)]
    reverse_mapper = [[] for _ in range(10001)]
    for word in words:
        origin_mapper[len(word)].append(word)
        reverse_mapper[len(word)].append(word[::-1])

    for i in range(10001):
        origin_mapper[i].sort()
        reverse_mapper[i].sort()

    for query in queries:
        if query[0] == "?":
            cnt = query.count("?")

            first_target = query[cnt:][::-1] + "a" * cnt
            last_target = query[cnt:][::-1] + "z" * cnt

            start_index = binary_search(reverse_mapper[len(query)], first_target)
            answer.append(count_match_word(reverse_mapper[len(query)], start_index, last_target))
        else:
            cnt = query.count("?")

            first_target = query[:len(query) - cnt] + "a" * cnt
            last_target = query[:len(query) - cnt] + "z" * cnt

            start_index = binary_search(origin_mapper[len(query)], first_target)
            answer.append(count_match_word(origin_mapper[len(query)], start_index, last_target))

    return answer