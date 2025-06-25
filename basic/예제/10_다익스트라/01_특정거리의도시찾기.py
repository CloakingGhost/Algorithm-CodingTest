# https://www.acmicpc.net/problem/18352
import sys
from heapq import heappop, heappush


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]  # dist, node

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > k:
            break
        elif distance[node] == k:
            answer.append(node)

        for next_node, dist in graph[node]:
            next_dist = dist + min_dist

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))


input = sys.stdin.readline

INF = float("inf")
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
answer = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

dijkstra(x)
if answer:
    print(*answer, sep="\n")
else:
    print(-1)
