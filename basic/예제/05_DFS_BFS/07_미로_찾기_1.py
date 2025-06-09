import sys

# 다른 언어는 재귀의 제한이 없어서
# 시험때는 신경안써도 됨
sys.setrecursionlimit(10**6)


def solution(maze):
    def dfs(x, y):
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위, 방문확인, 통로인지(문제의 조건)
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not maze[nx][ny]:
                # 비효율적인 반복을 줄이기 위함
                if nx == n - 1 and ny == n - 1:
                    # 외부 함수의 변수 변경시 사용
                    nonlocal answer
                    answer = True
                    return
                visited[nx][ny] = True
                dfs(nx, ny)

    n = len(maze)

    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 정점이 이차원 배열로 되어 있기 때문
    visited = [[False] * n for _ in range(n)]
    answer = False

    visited[0][0] = True

    dfs(x, y)  # 인덱스로 정점번호를 대신함

    return answer


from collections import deque


def solution(maze):
    def bfs(x, y):
        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
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
                        answer = True
                        return
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    n = len(maze)
    visited = [[False] * n for _ in range(n)]
    answer = False
    bfs(0, 0)
    return answer
