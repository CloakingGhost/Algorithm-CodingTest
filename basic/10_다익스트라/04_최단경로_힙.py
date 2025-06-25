import sys
from heapq import heappush, heappop


input = sys.stdin.readline


# O(E logE): 완전그래프 일 때
# O(E logV): 일반적으로 정점이 더 적기 때문
def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)  # 후보를 꺼냄

        # 이미 start -> node 까지의 거리가 후보 거리보다 작다면,
        # 그 후보 거리로부터는 알아낼 수 있는 여지가 없으므로 continue
        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            # next_dist = distance[node] + dist
            next_dist = min_dist + dist

            # next_node로 갈 수 있는 최단 거리를 찾았다면,
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist  # next_node에 대한 최단 거리 갱신
                # next_node를 통해서 또 다른 최단 거리를 찾을 수 잇는 여지가 있기 때문에
                # 힙에 삽입
                heappush(heap, (next_dist, next_node))


n, m = map(int, input().split())
start = int(input())

INF = float("inf")
distance = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)

# 경로가 존재하지 않으면 INF
# == 갈수가 없으면 INF
# 처음에 설정한 INF가 유지됐기 때문에
# 변경될 일이 없었기 때문에
# 출력도 INF로 나옴
for dist in distance[1:]:
    if dist == INF:
        print("INF")
    else:
        print(dist)
