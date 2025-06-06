# https://school.programmers.co.kr/learn/courses/30/lessons/120866?language=python3


def solution(board):
    # 상 우상 우 우하 하 좌하 좌 좌상
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    n = len(board)

    check_board = [[True] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 지뢰의 위치인 경우
            if board[i][j]:
                check_board[i][j] = False
                # 탐색
                for d in range(8):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and check_board[nx][ny]:
                        check_board[nx][ny] = False

    return sum(map(sum, check_board))


print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)
print(
    solution(
        [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]
    )
)
