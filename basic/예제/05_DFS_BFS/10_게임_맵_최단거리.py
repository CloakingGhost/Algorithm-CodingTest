# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    def bfs(x, y):
        queue = deque([(x, y, 1)])
        visited = [[False] * m for _ in range(n)]
        visited[x][y] = True

        while queue:
            x, y, dist = queue.popleft()

            if x == n - 1 and y == m - 1:
                return dist

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and maps[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

        return -1

    return bfs(0, 0)


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
        ]
    )
)
