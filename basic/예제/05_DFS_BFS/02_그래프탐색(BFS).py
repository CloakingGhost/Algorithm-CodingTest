# https://dailyalgo.kr/ko/problems/28

from collections import deque


def solution(n, edges):

    # 너비우선탐색
    def bfs(node):
        queue = deque([node])

        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

    # 1. 인접리스트로 그래프 구현
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 2. 방문 리스트
    visited = [False] * (n + 1)

    # 3. bfs 시작
    visited[1] = True
    bfs(1)
    return sum(visited)


print(solution(6, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 5]]))
print(
    solution(
        10,
        [
            [1, 2],
            [1, 4],
            [1, 6],
            [2, 3],
            [3, 4],
            [3, 7],
            [4, 5],
            [5, 6],
            [5, 7],
            [5, 8],
            [9, 10],
        ],
    )
)
print(solution(2, [[1, 2]]))
