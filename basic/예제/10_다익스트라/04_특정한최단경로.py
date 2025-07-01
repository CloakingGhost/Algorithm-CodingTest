# https://www.acmicpc.net/problem/1504
import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(start):
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            next_dist = min_dist + dist
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))

    return distance


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
INF = float("inf")

v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_route = v1_distance[1] + v1_distance[v2] + v2_distance[n]
v2_route = v2_distance[1] + v2_distance[v1] + v1_distance[n]
answer = min(v1_route, v2_route)

if answer == INF:
    print(-1)
else:
    print(answer)


"""
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

4 3
1 2 3
2 3 3
1 3 5
2 3

4 1
1 2 3
2 3

"""
