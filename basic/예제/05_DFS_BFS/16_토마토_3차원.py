# https://www.acmicpc.net/problem/7569

import sys
from collections import deque


input = sys.stdin.readline

# 상수 정의
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
EMPTY, UNRIPE, RIPE = -1, 0, 1


def is_in_bounds(x, y, z, n, m, h):
    return 0 <= x < n and 0 <= y < m and 0 <= z < h


def has_unripe_tomato(boxs):
    return any(0 in row for box in boxs for row in box)


def bfs(tomatos):
    queue = deque(tomatos)
    while queue:
        z, x, y, t = queue.popleft()
        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]
            if is_in_bounds(nx, ny, nz, n, m, h) and boxs[nz][nx][ny] == UNRIPE:
                boxs[nz][nx][ny] = RIPE
                queue.append((nz, nx, ny, t + 1))

    return -1 if has_unripe_tomato(boxs) else t


m, n, h = map(int, input().split())

boxs = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
tomatos = [
    (i, j, k, 0)
    for i in range(h)
    for j in range(n)
    for k in range(m)
    if boxs[i][j][k] == RIPE
]

print(bfs(tomatos))
"""
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 0

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
"""
