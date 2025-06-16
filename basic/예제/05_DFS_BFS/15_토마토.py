# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline

# 상수 정의
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
EMPTY, UNRIPE, RIPE = -1, 0, 1


def has_unripe_tomato(box):
    return any(UNRIPE in row for row in box)


def is_in_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def bfs(box, tomatos, n, m):
    queue = deque(tomatos)

    while queue:
        x, y, t = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if is_in_bounds(x, y, n, m) and box[nx][ny] == UNRIPE:
                box[nx][ny] = RIPE
                queue.append((nx, ny, t + 1))

    return EMPTY if has_unripe_tomato(box) else t


# 입력 처리
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
time = 0
tomatos = [(i, j, time) for i in range(n) for j in range(m) if box[i][j] == RIPE]

# 결과 출력
print(bfs(box, tomatos, n, m))

"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""
