# https://www.acmicpc.net/problem/1012
import sys

sys.setrecursionlimit(10**6)
from collections import deque

input = sys.stdin.readline


def dfs(x, y, ground, n, m):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and ground[nx][ny]:
            ground[nx][ny] = 0
            dfs(nx, ny, ground, n, m)


def bfs(x, y, ground, n, m):
    queue = deque([(x, y)])
    bugs = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and ground[nx][ny]:
                ground[nx][ny] = 0
                queue.append((nx, ny))


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    ground = [[0] * m for _ in range(n)]
    bugs = 0
    for _ in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1

    for i in range(n):
        for j in range(m):
            if ground[i][j]:
                bugs += 1
                ground[i][j] = 0
                bfs(i, j, ground, n, m)

    print(bugs)

"""
얼음 정수기
15만원

지금은 10만원 상품권

요즘은 스탱으로 6개월마다 방문

28900 일반정수기에서 살균만
옵션에 따라 금액이 다르니까

"""
