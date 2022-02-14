from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    cities = list(map(lambda x: x.lower(), cities))
    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            answer += 5
            cache.append(city)
    return answer
