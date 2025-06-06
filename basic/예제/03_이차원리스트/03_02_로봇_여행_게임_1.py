def solution_old(board, queries):
    n, m = len(board), len(board[0])
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = 0, 0
    answer = 0
    for q in queries:
        if q == "Get Score":
            answer += board[x][y]
            continue

        if q == "Move Up":
            direction = 0
        elif q == "Move Down":
            direction = 1
        elif q == "Move Left":
            direction = 2
        elif q == "Move Right":
            direction = 3
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < m:
            x = nx
            y = ny

    return answer


def solution(board, queries):
    n, m = len(board), len(board[0])
    # 상하좌우
    command = {
        "Move Up": (-1, 0),
        "Move Down": (1, 0),
        "Move Left": (0, -1),
        "Move Right": (0, 1),
    }
    x, y = 0, 0
    answer = 0
    for q in queries:
        if q == "Get Score":
            answer += board[x][y]
        else:
            dx, dy = command.get(q)
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                x = nx
                y = ny

    return answer


board = [[10, 20, 16], [8, 6, 11], [10, 2, 12]]
queries = ["Move Left", "Move Right", "Get Score", "Move Right", "Move Down"]
print(solution(board, queries))  # 16
