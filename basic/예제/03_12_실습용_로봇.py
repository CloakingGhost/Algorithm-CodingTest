# https://school.programmers.co.kr/learn/courses/20848/lessons/255904?language=python3


def solution(command):
    x, y = 0, 0
    direction = 0

    # 상 우 하 좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for c in command:
        if c == "R":
            direction = (direction + 1) % 4
        elif c == "L":
            direction = (direction - 1) % 4
        elif c == "G":
            x += dx[direction]
            y += dy[direction]
        elif c == "B":
            x -= dx[direction]
            y -= dy[direction]

    return [x, y]


print(solution("GRGLGRG"))
print(solution("GRGRGRB"))
