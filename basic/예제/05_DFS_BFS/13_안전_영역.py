import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y, h, n, board, visited):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] <= h:
            visited[nx][ny] = True
            dfs(nx, ny, h, n, board, visited)


def check_safe_area(x, y, visited):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True

            check_safe_area(nx, ny, visited)


dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

n = int(input())
board = []
max_height = 0
answer = 1
for _ in range(n):
    line = list(map(int, input().split()))
    max_height = max(*line, max_height)
    board.append(line)

for h in range(1, max_height):
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] <= h:
                # print(f"i, j, board[i][j] : {i}, {j}, {board[i][j]}")
                visited[i][j] = True
                dfs(i, j, h, n, board, visited)
    # print(f"h: {h}")
    # print(*visited, sep="\n")
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                count += 1
                check_safe_area(i, j, visited)
    # print(f"count: {count}")
    answer = max(answer, count)
# print(f"answer: {answer}")
print(answer)

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

2
1 1
1 1

"""
import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx, ny)


dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

n = int(input())
board = []
heights = set()
answer = 1
for _ in range(n):
    line = list(map(int, input().split()))
    heights.update(line)
    board.append(line)

for h in heights:
    visited = [[False] * n for _ in range(n)]
    safe_area = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > h:
                safe_area += 1
                visited[i][j] = True
                dfs(i, j)
    answer = max(answer, safe_area)
print(answer)
