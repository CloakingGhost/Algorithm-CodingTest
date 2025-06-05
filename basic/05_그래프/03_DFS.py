# 깊이우선 탐색(Depth-First Search, DFS)

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
n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# print(*graph, sep='\n')

# 2. 방문 리스트 (visited)
visited = [False] * n


# 3. 깊이우선탐색 진행
## 더이상 갈 곳이 없으면 pop
def dfs(node):
    print(node)  # 현재 방문 정점 출력

    # 인접한 정점 중 방문하지 않은 곳으로 이동
    print(graph[node])  # 점정의 인접리스트
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)


visited[0] = True  # 출발점
dfs(0)  # 출발정점에서 DFS 시작
