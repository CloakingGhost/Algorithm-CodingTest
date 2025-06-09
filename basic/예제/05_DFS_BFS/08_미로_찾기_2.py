# https://dailyalgo.kr/ko/problems/63
import sys

sys.setrecursionlimit(10**6)


# 실패 코드
def solution(maze):
    n = len(maze)

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    # O(2**N**2)
    # 다시 돌아감
    def dfs(x, y, depth):
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not maze[nx][ny]:
                if nx == n - 1 and ny == n - 1:
                    nonlocal answer
                    answer = min(answer, depth + 1)
                    return

                visited[nx][ny] = True
                dfs(nx, ny, depth + 1)
                visited[nx][ny] = False  # 돌아올때 방문지도 취소 해야함

    visited = [[False] * n for _ in range(n)]

    answer = n * n
    dfs(0, 0, 0)  # 시작점
    return answer


print(solution([[0, 0, 1], [1, 0, 0], [1, 0, 0]]))
print(solution([[0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 1, 0]]))
print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
        ]
    )
)

from collections import deque


def solution(maze):
    n = len(maze)

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    # 다시 돌아가지 않음
    def bfs(x, y):
        queue = deque([(x, y, 0)])
        while queue:
            x, y, distence = queue.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and not visited[nx][ny]
                    and not maze[nx][ny]
                ):
                    if nx == n - 1 and ny == n - 1:
                        nonlocal answer
                        answer = min(answer, distence + 1)
                        return
                    visited[nx][ny] = True
                    queue.append((nx, ny, distence + 1))

    visited = [[False] * n for _ in range(n)]

    answer = n * n
    bfs(0, 0)  # 시작점
    return answer
