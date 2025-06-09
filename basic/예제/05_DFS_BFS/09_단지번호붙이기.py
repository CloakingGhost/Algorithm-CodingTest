# https://www.acmicpc.net/problem/2667
import sys

input = sys.stdin.readline


def dfs(i, j):
    count = 1
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if 0 <= nx < n and 0 <= ny < n and apartment[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            count += dfs(nx, ny)

    return count


n = int(input())
apartment = [list(map(int, input().rstrip())) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[False] * n for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        if apartment[i][j] and not visited[i][j]:
            visited[i][j] = True
            answer.append(dfs(i, j))

print(len(answer), *sorted(answer), sep="\n")

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
import sys

input = sys.stdin.readline


def dfs(i, j):
    count = 1
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if 0 <= nx < n and 0 <= ny < n and apartment[nx][ny]:
            apartment[nx][ny] = 0
            count += dfs(nx, ny)

    return count


n = int(input())
apartment = [list(map(int, input().rstrip())) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = []
for i in range(n):
    for j in range(n):
        if apartment[i][j]:
            apartment[i][j] = 0
            answer.append(dfs(i, j))

print(len(answer), *sorted(answer), sep="\n")


from collections import deque


def bfs(i, j):
    count = 1
    queue = deque([(i, j)])

    while queue:
        i, j = queue.popleft()
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if 0 <= nx < n and 0 <= ny < n and apartment[nx][ny]:
                apartment[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
apartment = [list(map(int, input().rstrip())) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = []
for i in range(n):
    for j in range(n):
        if apartment[i][j]:
            apartment[i][j] = 0
            answer.append(bfs(i, j))

print(len(answer), *sorted(answer), sep="\n")
