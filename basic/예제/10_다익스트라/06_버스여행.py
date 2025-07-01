from heapq import heappop, heappush


def solution(cities, buses, dest):
    def calc_distance(p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return (dx * dx + dy * dy) ** 0.5 / 100

    def dijkstra(start):
        distance[start] = 0
        heap = [(0, start)]

        while heap:
            min_dist, node = heappop(heap)
            if min_dist > distance[node]:
                continue
            # 현재 노드와 연결된 모든 노드 탐색
            for next_node in range(n):
                if node == next_node:  # 자기 자신 제외
                    continue
                next_dist = min_dist + graph[node][next_node]
                # 더 짧은 경로 발견 시 업데이트
                if next_dist < distance[next_node]:
                    distance[next_node] = next_dist
                    heappush(heap, (next_dist, next_node))

    cities = [[0, 0]] + cities  # 시작점 추가 (0번 노드)
    n = len(cities)
    INF = float("inf")

    # 그래프 초기화 (인접 행렬)
    graph = [[INF] * n for _ in range(n)]

    # 1. 모든 노드 쌍에 대한 걷기 시간 계산
    for i in range(n):
        # 대칭 구조 활용: j = i부터 시작하여 중복 계산 방지
        for j in range(i, n):
            if i == j:
                graph[i][j] = 0
                continue
            walk_time = calc_distance(cities[i], cities[j])
            graph[j][i] = graph[i][j] = walk_time

    # 2. 버스 시간 업데이트 (양방향)
    for s, e, t in buses:
        # 버스 시간이 기존 시간보다 작을 때만 업데이트
        if t < graph[s][e]:
            graph[s][e] = graph[e][s] = t

    # 3. 다익스트라 알고리즘
    distance = [INF] * n

    dijkstra(0)
    # 4. 소수점 셋째 자리 버림 처리
    return int(distance[dest] * 1000) / 1000


print(
    solution(
        [[-5.457, -13.456], [93.551, -98.776], [92.740, 87.973], [89.438, 87.416]],
        [[1, 3, 1], [4, 1, 1]],
        3,
    )
)

print(
    solution(
        [
            [-0.635, 97.175],
            [71.424, 97.484],
            [-54.368, -85.041],
            [48.631, 89.916],
            [-93.897, 38.331],
        ],
        [[1, 4, 1], [2, 3, 1], [3, 4, 1]],
        4,
    )
)
