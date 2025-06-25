# https://www.acmicpc.net/problem/14938
import sys
from heapq import heappop, heappush


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]  # 최단 거리, node

    while heap:
        min_dist, node = heappop(heap)

        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            next_dist = dist + min_dist

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))


input = sys.stdin.readline
n, m, r = map(int, input().split())  # 정점, 수색가능범위, 간선
# 시작정점 1이 아닌 0 으로
item = list(map(int, input().split()))  # 정점 만큼
INF = float("inf")
graph = [[] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))

answer = 0

for start in range(n):

    distance = [INF] * n
    dijkstra(start)

    total = sum(item[i] for i in range(n) if distance[i] <= m)
    answer = max(total, answer)

print(answer)

"""
5 5 4
5 7 8 2 3
1 4 5
5 2 4
3 2 3
1 2 3
"""
