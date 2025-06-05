def solution(n, edges):

    def dfs(node):
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dfs(next_node)

    # 1. 인접리스트 그래프 구현
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    # 2. 방문 리스트
    visited = [False] * (n + 1)

    # 3. dfs 시작
    visited[1] = True
    dfs(1)

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
