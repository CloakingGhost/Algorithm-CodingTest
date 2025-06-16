# https://www.acmicpc.net/problem/2206
import sys
from collections import deque


input = sys.stdin.readline

# 상수
ROAD, WALL = 0, 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        pass


n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
