from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cities = [city.lower() for city in cities]
    cache = deque()
    time = 0

    for i in range(len(cities)):
        if cities[i] in cache:
            cache.remove(cities[i])
            cache.append(cities[i])
            time += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(cities[i])
            time += 5

    return time
