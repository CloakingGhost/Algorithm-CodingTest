# https://school.programmers.co.kr/learn/courses/30/lessons/120861?language=python3


def solution(keyinput, board):
    command = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}

    n, m = board
    width, height = n >> 1, m >> 1
    x, y = 0, 0

    for input in keyinput:
        dx, dy = command.get(input)
        nx, ny = x + dx, y + dy
        if -(width) <= nx <= width and -(height) <= ny <= height:
            x, y = nx, ny

    return [x, y]


print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))
