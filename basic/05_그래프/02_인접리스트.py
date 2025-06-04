# 인접리스트
"""
0 1
0 2
0 5
0 6
3 4
3 5
4 5
4 6

간선 정보 => 그래프
공간 낭비가 심하다 : 공간복잡도가 높다

정점과 인접되어 있는 정점만 담는다
2차원리스트의 형태
"""
# 무방향 그래프
n = 7  # 정점의 개수
m = 8  # 간선의 개수

graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
print(*graph, sep="\n")

print()

# 유방향 그래프
n = 7  # 정점의 개수
m = 8  # 간선의 개수

graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
print(*graph, sep="\n")
