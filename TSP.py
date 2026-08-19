import itertools
import math
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 +
                     (city1[1] - city2[1]) ** 2)
def tsp(cities):
    start = cities[0]
    remaining = cities[1:]
    min_distance = float('inf')
    best_path = None
    for perm in itertools.permutations(remaining):
        path = [start] + list(perm) + [start]
        total = 0
        for i in range(len(path) - 1):
            total += distance(path[i], path[i + 1])
        if total < min_distance:
            min_distance = total
            best_path = path
    return min_distance, best_path
cities = [(1, 2), (4, 5), (7, 1), (3, 6)]
d, path = tsp(cities)

print("Minimum Distance:", d)
print("Best Path:", path)