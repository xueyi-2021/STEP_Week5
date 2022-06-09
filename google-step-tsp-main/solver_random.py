#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input, distance, total_distance


def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.
    return list(range(len(cities)))


'''
def distance(city1, city2):
    return math.sqrt(pow((city1[0] - city2[0]), 2) + pow((city1[1] - city2[1]), 2))
'''

'''
def total_distance(tour, cities):
    result = 0
    for i in range(len(tour) - 1):
        result += distance(cities[i], cities[i + 1])
    return result
'''

if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    tour = solve(cities)
    print_tour(tour)
    print(total_distance(tour, cities))