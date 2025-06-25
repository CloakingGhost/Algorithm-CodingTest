# https://dailyalgo.kr/ko/problems/29
# 다익스트라(dijkstra)


def solution(n, edges):
    def dijkstra(start):
        # 3. distance[출발점] = 0 할당
        distance[start] = 0

        for _ in range(
            n - 1
        ):  # n - 1 번만 반복해도 n번째 정점에 대한 최단거리가 확정됨
            # 4. distance에서 최소값을 찾음
            node, min_dist = -1, INF

            for i in range(1, n + 1):
                if not visited[i] and min_dist > distance[i]:
                    node = i
                    min_dist = distance[i]

            # 5. 최소 거리 노드에 대해 거리 확정
            visited[node] = True

            # 6. 인접 노드들에 대해 거리를 더 작은 값으로 갱신
            for next_node, dist in graph[node]:
                next_dist = distance[node] + dist

                # 최단거리 확정 안되고 거리가 짧을 때
                if not visited[next_node] and next_dist < distance[next_node]:
                    distance[next_node] = next_dist

    INF = float("inf")
    distance = [INF] * (n + 1)  # 1. distance를 무한대로 초기화
    visited = [False] * (
        n + 1
    )  # 2. visited를 False로 모두 초기화(최단거리 확정된 곳이 없음)

    graph = [[] for _ in range(n + 1)]

    for x, y, w in edges:
        graph[x].append((y, w))

    dijkstra(1)

    # print(distance)

    return distance[n]


print(
    solution(
        5,
        [[1, 2, 3], [3, 5, 1], [1, 5, 10], [4, 5, 3], [2, 4, 1], [3, 4, 4], [1, 3, 2]],
    )
)

print(
    solution(
        8,
        [
            [5, 8, 4],
            [4, 8, 4],
            [3, 4, 8],
            [4, 5, 4],
            [2, 3, 3],
            [7, 5, 8],
            [3, 7, 2],
            [3, 5, 6],
            [3, 1, 2],
            [4, 2, 8],
            [2, 8, 15],
            [6, 3, 9],
            [3, 6, 7],
            [1, 7, 8],
            [1, 2, 3],
        ],
    )
)
