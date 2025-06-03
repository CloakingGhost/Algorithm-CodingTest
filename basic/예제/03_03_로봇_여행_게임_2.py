# https://dailyalgo.kr/ko/problems/74


def solution(board, queries):
    n = len(board)
    m = len(board[0])

    # 1. 기준점 잡기
    x, y = 0, 0
    # 2. 델타값 정의(하 우 상 좌)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    direction = 0
    answer = 0

    # 3. 명령어 처리
    for q in queries:
        if q == "Get Score":
            answer += board[x][y]
            continue

        if q == "Turn Left":
            direction = (direction + 1) % 4
            continue

        if q == "Turn Right":
            direction = (4 + direction - 1) % 4
            continue

        if q == "Move Forward":
            nx = x + dx[direction]
            ny = y + dy[direction]
        elif q == "Move Backward":
            nx = x - dx[direction]
            ny = y - dy[direction]

        # 4. 범위 확인 및 이동
        if 0 <= nx < n and 0 <= ny < m:
            x = nx
            y = ny
    return answer


board = [[15, 1, 6], [4, 6, 17], [2, 16, 17], [18, 8, 8], [5, 17, 10]]

queries = [
    "Get Score",
    "Move Forward",
    "Move Forward",
    "Turn Left",
    "Move Backward",
    "Get Score",
    "Get Score",
    "Move Forward",
    "Get Score",
]
print(solution(board, queries))  # 11
