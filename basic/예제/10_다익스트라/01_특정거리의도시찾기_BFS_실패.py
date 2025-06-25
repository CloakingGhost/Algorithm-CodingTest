# https://www.acmicpc.net/problem/18352
import sys
from collections import deque


def bfs(start):
    queue = deque([(start, 0)])  # node, depth

    while queue:
        node, dist = queue.popleft()

        # print(f"node, dist, visited[node]: {node, dist, visited[node]}")
        if dist > k:
            break

        elif dist == k:
            answer.append(node)

        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append((next_node, dist + 1))
                visited[next_node] = True


input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# print(graph)
visited[x] = True
bfs(x)
if answer:
    print(*answer, sep="\n")
else:
    print(-1)
