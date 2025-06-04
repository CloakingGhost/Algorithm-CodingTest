# https://school.programmers.co.kr/learn/courses/30/lessons/68645?language=python3


def solution(n):
    triangle_snail = [[0] * i for i in range(1, n + 1)]

    # 하 우 좌상
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    direction = 0

    x, y = -1, 0  # 가정: 아래 방향으로 외부에서 진입
    limit = (n + 1) * n // 2
    for i in range(1, limit + 1):
        nx = x + dx[direction]
        ny = y + dy[direction]

        # nx행의 열 개수
        # 범위에 없거나, 숫자가 있으면 => 방향, 좌표 변경
        if (
            not (0 <= nx < n and 0 <= ny < len(triangle_snail[nx]))
            or triangle_snail[nx][ny]
        ):
            direction = (direction + 1) % 3
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny
        triangle_snail[x][y] = i
    return [num for row in triangle_snail for num in row]


print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
