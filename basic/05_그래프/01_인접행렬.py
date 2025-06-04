# 인접행렬
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
"""

# 무방향 그래프
n = 7  # 정점의 개수
m = 8  # 간선의 개수

# 1. 그래프 초기화
## 모든 정점간의 관계를 표현하기 위해 정점의 개수 만큼 리스트 초기화
graph = [[0] * n for _ in range(n)]

## 2. 간선 개수 만큼 반복하여 정점 간 관계를 행렬에 표시
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

print(*graph, sep="\n")


print()

n = 7  # 정점의 개수
m = 8  # 간선의 개수

# 1. 그래프 초기화
## 모든 정점간의 관계를 표현하기 위해 정점의 개수 만큼 리스트 초기화
graph = [[0] * n for _ in range(n)]

## 2. 간선 개수 만큼 반복하여 정점 간 관계를 행렬에 표시
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1

print(*graph, sep="\n")
