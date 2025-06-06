# 너비우선탐색 (Breadth-First Search, BFS)

# 1. 그래프 구현 (인전리스트)
"""
7 7
0 1
0 2
1 3
1 4
2 4
2 5
4 6
"""
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 2. 방문 리스트(visited)
visited = [False] * m

# 3. BFS 진행
from collections import deque


def bfs(node):
    queue = deque([node])  # 큐에 출방정점을 넣고 시작

    # 큐가 비어있지 않으면 탐색을 지속하고,
    # 큐가 비면 탐색을 종료
    while queue:
        node = queue.popleft()  # 실제 뺄 때 방문
        for next_node in graph[node]:  # 인접한 정점들에 대해
            if not visited[node]:  # 방문하지 않은 점점에 대해
                visited[next_node] = (
                    True  # 이동할 정점 방문처리: 해당 정점을 공통으로 가진 정점이 큐에 중복으로 넣기 때문
                )
                queue.append(next_node)  # 이동할 정점 큐에 삽입


visited[0] = True
bfs(0)
