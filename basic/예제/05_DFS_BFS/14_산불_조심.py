# https://dailyalgo.kr/ko/problems/65
from collections import deque


def bfs_old(x, y, mountain, n):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    time = 0
    queue = deque([(x, y, time)])
    while queue:
        x, y, t = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and mountain[nx][ny] == 0:
                mountain[nx][ny] = 2
                queue.append((nx, ny, t + 1))
                time = max(time, t + 1)
                print(f"t: {t}")
                print(*mountain, sep="\n")
    return time


def solution_old(mountain):
    n = len(mountain)
    fires = set()
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == 2:
                fires.add((i, j))
    answer = 0

    for x, y in fires:
        answer = max(answer, bfs(x, y, mountain, n))

    return answer


def bfs(fires, mountain, n):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    time = 0
    queue = deque(fires)
    while queue:
        x, y, t = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and mountain[nx][ny] == 0:
                mountain[nx][ny] = 2
                queue.append((nx, ny, t + 1))
                time = t + 1
    return time


def solution(mountain):
    n = len(mountain)
    fires = [(i, j, 0) for i in range(n) for j in range(n) if mountain[i][j] == 2]

    return bfs(fires, mountain, n)


print(solution([[2, 1, 0, 1], [0, 1, 1, 1], [1, 0, 1, 1], [0, 2, 0, 2]]))
print(
    solution(
        [
            [0, 1, 0, 1, 1],
            [0, 0, 1, 0, 2],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)
print(solution([[2, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 2, 1]]))
print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)
