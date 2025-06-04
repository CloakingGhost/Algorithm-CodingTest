# https://school.programmers.co.kr/learn/courses/30/lessons/81302#fn1

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_old(room, n):
    for x in range(n):
        for y in range(n):

            if room[x][y] == "P":

                # 1차 델타 탐색
                for d_1 in range(4):
                    nx_1 = x + dx[d_1]
                    ny_1 = y + dy[d_1]
                    if 0 <= nx_1 < n and 0 <= ny_1 < n:

                        # 연속 "P"
                        if room[nx_1][ny_1] == "P":
                            return 0

                        # 2차 델타 탐색
                        elif room[nx_1][ny_1] == "O":
                            for d_2 in range(4):
                                nx_2 = nx_1 + dx[d_2]
                                ny_2 = ny_1 + dy[d_2]
                                if (
                                    not (nx_2 == x and ny_2 == y)  # 원래위치 제외
                                    and 0 <= nx_2 < n
                                    and 0 <= ny_2 < n
                                    and room[nx_2][ny_2] == "P"
                                ):
                                    return 0
    return 1


def check(room, n):
    # 문자열은 불변객체
    # 배열변환하여 변경
    room = [list(line) for line in room]
    for x in range(n):
        for y in range(n):

            if room[x][y] == "P":

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:

                        # 연속 "P"
                        if room[nx][ny] in "PA":
                            return 0

                        # 마킹
                        # 다음 P에서 델타탐색 중
                        # A를 발견하면 맨해튼 거리 2 안에 있음
                        if room[nx][ny] == "O":
                            room[nx][ny] = "A"
    return 1


def solution(places):
    n = len(places)

    return [check(room, n) for room in places]


# print(
#     solution(
#         [
#             ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#             ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#             ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#             ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#             ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
#         ]
#     )
# )

a = "PXPXP"
a[0] = "2"
print(a)
