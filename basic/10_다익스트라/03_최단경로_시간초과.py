import sys


input = sys.stdin.readline


# O(V**2)
def dijkstra(start):
    distance[start] = 0

    for _ in range(n - 1):
        node, min_dist = -1, INF

        for next_node in range(1, n + 1):
            if not visited[next_node] and distance[next_node] < min_dist:
                node = next_node
                min_dist = distance[next_node]

        visited[node] = True

        for next_node, dist in graph[node]:
            next_dist = distance[node] + dist
            if not visited[next_node] and next_dist < distance[next_node]:
                distance[next_node] = next_dist


n, m = map(int, input().split())
start = int(input())

INF = float("inf")
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

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
