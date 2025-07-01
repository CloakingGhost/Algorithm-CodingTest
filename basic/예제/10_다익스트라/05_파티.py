# https://www.acmicpc.net/problem/1238
import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(start, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            next_dist = dist + min_dist
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))
    return distance


INF = float("inf")
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reversed_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    reversed_graph[e].append((s, t))

to_home_distance = dijkstra(x, graph)
to_x_distance = dijkstra(x, reversed_graph)
answer = 0


print(max(map(sum, zip(to_x_distance[1:], to_home_distance[1:]))))
