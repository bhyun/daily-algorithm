from collections import defaultdict
def solution(genres, plays):
    answer = []
    songs = defaultdict(list)
    count = defaultdict(int)
    i = 0
    for g, p in zip(genres, plays):
        songs[g].append((i, p))
        count[g] += p
        i += 1
    order = sorted(count, key=count)
    print(order)

