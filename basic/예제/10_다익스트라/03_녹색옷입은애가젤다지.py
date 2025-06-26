# https://www.acmicpc.net/problem/4485
import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(x, y):
    distance[x][y] = matrix[x][y]
    heap = [(matrix[x][y], (x, y))]

    while heap:
        min_thief_rupee, current = heappop(heap)
        x, y = current

        if x == n and y == n:
            return

        if min_thief_rupee > distance[x][y]:
            continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            next_thief_rupee = min_thief_rupee + matrix[nx][ny]

            if matrix[nx][ny] >= 0 and next_thief_rupee < distance[nx][ny]:
                distance[nx][ny] = next_thief_rupee
                heappush(heap, (next_thief_rupee, (nx, ny)))


# 상하좌우
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


case = 1
while True:
    n = int(input())
    if n == 0:
        break
    # Boundary Padding(경계 패딩) : 인덱스 범위 체크 제거
    matrix = (
        [[-1] * (n + 2)]
        + [[-1] + list(map(int, sys.stdin.readline().split())) + [-1] for _ in range(n)]
        + [[-1] * (n + 2)]
    )

    distance = [[float("inf")] * (n + 2) for _ in range(n + 2)]

    dijkstra(1, 1)
    print(f"Problem {case}: {distance[n][n]}")
    case += 1

"""
3
0 0 1
0 0 1
1 1 1
0
"""
