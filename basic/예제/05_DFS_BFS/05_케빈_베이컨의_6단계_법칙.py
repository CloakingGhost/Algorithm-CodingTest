# https://www.acmicpc.net/problem/1389

import sys
from collections import deque

input = sys.stdin.readline


def bfs(node, dist):

    queue = deque([(node, dist)])

    while queue:
        node, dist = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = dist + 1
                queue.append((next_node, dist + 1))


# 1. 그래프 구현
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 1-1. 중복 제거
for idx, friends in enumerate(graph):
    graph[idx] = list(set(friends))


# 3. 탐색
dist = 0
answer = {}
for node in range(1, n + 1):
    # 2. 방문지: 각 노드마다 새롭게 탐색
    visited = [0] * (n + 1)
    if not visited[node]:
        visited[node] = True
        bfs(node, dist)
        answer[node] = sum(visited)

print(answer)
print(sorted(answer, key=lambda x: answer[x]))
print(sorted(answer, key=lambda x: answer[x])[0])
"""
5 5
1 3
1 4
4 5
4 3
3 2
"""
"""
5 5
1 2
1 3
1 4
1 5
1 5
"""
#######################################

import sys
from collections import deque

input = sys.stdin.readline


def dfs(node, dist):
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = dist + 1
            dfs(next_node, dist + 1)


# 1. 그래프 구현
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 1-1. 중복 제거
for idx, friends in enumerate(graph):
    graph[idx] = list(set(friends))


# 3. 탐색
dist = 0
answer = {}
for node in range(1, n + 1):
    # 2. 방문지: 각 노드마다 새롭게 탐색
    visited = [False] * (n + 1)
    if not visited[node]:
        visited[node] = 1
        dfs(node, dist)
        answer[node] = sum(visited)

print(answer)
print(sorted(answer, key=lambda x: answer[x]))
print(sorted(answer, key=lambda x: answer[x])[0])
