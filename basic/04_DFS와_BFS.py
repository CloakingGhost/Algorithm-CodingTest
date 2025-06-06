# https://www.acmicpc.net/problem/1260

"""
4 5 1
3 4
2 4
1 4
1 3
1 2

"""
import sys
from collections import deque

input = sys.stdin.readline


def dfs(node):
    print(node, end=" ")

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)


def bfs(node):
    queue = deque([node])
    ans = [node]

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                ans.append(next_node)
                queue.append(next_node)

    return ans


# 1. 그래프 구현
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for edge in graph:
    edge.sort()


# 2. 방문 리스트
visited = [False] * (n + 1)

# 3-1. dfs 시작
visited[v] = True
dfs(v)

print()

visited = [False] * (n + 1)

# 3-2. bfs 시작
visited[v] = True
bfs(v)
