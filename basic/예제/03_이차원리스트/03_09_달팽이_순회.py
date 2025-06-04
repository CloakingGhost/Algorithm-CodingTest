# https://dailyalgo.kr/ko/problems/75


def solution(n):
    snail_board = [[0] * n for _ in range(n)]

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction = 0
    x, y = 0, 0

    snail_board[x][y] = 1

    i = 2
    while i <= n**2:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if not (0 <= nx < n and 0 <= ny < n) or snail_board[nx][ny]:
            direction = (direction + 1) % 4

        x = x + dx[direction]
        y = y + dy[direction]
        snail_board[x][y] = i
        i += 1
    return snail_board


# print(*solution(10), sep="\n")
