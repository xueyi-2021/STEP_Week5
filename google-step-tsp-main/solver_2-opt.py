#!/usr/bin/env python3

import sys

from common import print_tour, read_input, distance, total_distance


def solver_greedy(cities, current_city):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    #current_city = 0
    unvisited_cities = set(range(0, N))
    unvisited_cities.remove(current_city)
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour


def two_opt(tour, cities):
    tour.append(tour[0])  #処理しやすい

    while True:    #最初は1回だけループしたが、結果全然大きかったし交差点もいつくあった、多分何回もループして全ての交差点が消される
        count = 0
        for i in range(len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                #0->1->2->3のような経路は0->2->1->3に変換する
                #0->1と2->3の距離の和 と 0->2と1->3の距離の和 を比較する
                dis1 = distance(cities[tour[i]], cities[tour[i + 1]]) + distance(cities[tour[j]], cities[tour[j + 1]])  #交換前の距離
                dis2 = distance(cities[tour[i]], cities[tour[j]]) + distance(cities[tour[i + 1]], cities[tour[j + 1]])  #交換後の距離
                if dis2 < dis1:   #交換後の距離が小さいなら、交換する
                    temp = tour[i + 1:j + 1]
                    tour[i + 1:j + 1] = temp[::-1]
                    count += 1
        if count == 0:        #交換が発生しなかった = 交差点はもうない
            break

    tour.pop()  #最初appendしたのでここでpop
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    min_distance = 100000000
    if len(cities) > 500:
        for current_city in range(0, len(cities), 100):   #意味のないbrute forceです
            print(current_city)
            tour = solver_greedy(cities, current_city)
            new_tour = two_opt(tour, cities)
            t_d = total_distance(new_tour, cities)
            min_distance = min(min_distance, t_d)
        print(min_distance)
    else:
        for current_city in range(len(cities)):    #brute forceです ^_^
            tour = solver_greedy(cities, current_city)
            new_tour = two_opt(tour, cities)
            t_d = total_distance(new_tour, cities)
            min_distance = min(min_distance, t_d)
        print(min_distance)
