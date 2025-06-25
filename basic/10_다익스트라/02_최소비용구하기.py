import sys


def dijkstra(start, end):
    distance[start] = 0

    for _ in range(n - 1):
        node, min_dist = -1, INF

        for next_node in range(1, n + 1):
            if not visited[next_node] and distance[next_node] < min_dist:
                node = next_node
                min_dist = distance[next_node]
        visited[node] = True

        # 백트래킹
        if node == end:
            return

        for next_node, dist in graph[node]:
            next_dist = distance[node] + dist
            if not visited[next_node] and next_dist < distance[next_node]:
                distance[next_node] = next_dist


input = sys.stdin.readline

n, m = int(input()), int(input())

INF = float("inf")
distance = [INF] * (n + 1)
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))

start, end = map(int, input().split())
dijkstra(start, end)
print(distance[end])
