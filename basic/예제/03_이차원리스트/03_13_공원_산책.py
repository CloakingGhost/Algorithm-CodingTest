# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3


def solution(park, routes):
    n, m = len(park), len(park[0])

    command = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}

    x, y = next((i, j) for i in range(n) for j in range(m) if park[i][j] == "S")
    for r in routes:
        flag = True
        dire, dist = r[0], int(r[2])
        dx, dy = command.get(dire)
        for d in range(dist):
            nx = x + (dx * (1 + d))
            ny = y + (dy * (1 + d))
            # 범위안에 없고, 'X' 이면 => 반복문 탈출
            if not (0 <= nx < n and 0 <= ny < m and park[nx][ny] != "X"):
                flag = False
                break
        if flag:
            x += dx * dist
            y += dy * dist
    return [x, y]


print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
