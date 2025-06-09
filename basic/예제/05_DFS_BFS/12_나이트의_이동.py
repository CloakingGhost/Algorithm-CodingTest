# https://www.acmicpc.net/problem/7562

"""
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
"""

import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, visited, x, y, tx, ty):
    if x == tx and y == ty:
        return 0

    visited[x][y] = True
    queue = deque([(x, y, 0)])
    while queue:
        x, y, distance = queue.popleft()
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if nx == tx and ny == ty:
                    return distance + 1
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))


dx, dy = [-1, -2, -1, -2, 1, 2, 1, 2], [-2, -1, 2, 1, -2, -1, 2, 1]

t = int(input())

for _ in range(t):
    n = int(input())
    chess = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    x, y = map(int, input().split())  # 시작점
    tx, ty = map(int, input().split())  # 도착점

    print(bfs(n, visited, x, y, tx, ty))


import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, chess, x, y, tx, ty):
    if x == tx and y == ty:
        return 0

    queue = deque([(x, y)])
    chess[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not chess[nx][ny]:
                chess[nx][ny] = chess[x][y] + 1
                if nx == tx and ny == ty:
                    return chess[nx][ny] - 1
                queue.append((nx, ny))


dx, dy = [-1, -2, -1, -2, 1, 2, 1, 2], [-2, -1, 2, 1, -2, -1, 2, 1]

t = int(input())

for _ in range(t):
    n = int(input())
    chess = [[0] * n for _ in range(n)]

    x, y = map(int, input().split())  # 시작점
    tx, ty = map(int, input().split())  # 도착점

    print(bfs(n, chess, x, y, tx, ty))
