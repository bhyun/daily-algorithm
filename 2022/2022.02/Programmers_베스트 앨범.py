from collections import defaultdict

def solution(genres, plays):
    answer = []
    length = range(len(genres))

    genre_mapper = defaultdict(list)
    genres_sum_mapper = defaultdict(int)
    song_mapper = defaultdict(int)

    for l, g, p in zip(length, genres, plays):
        genre_mapper[g].append(l)
        genres_sum_mapper[g] += p
        song_mapper[l] = p

    for k in sorted(genres_sum_mapper, key=lambda x: genres_sum_mapper[x], reverse=True):
        temp = dict(filter(lambda x: x[0] in genre_mapper[k], song_mapper.items()))
        keys = sorted(temp.keys(), key=lambda x: (-temp[x], x))
        answer += keys[:2]

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))