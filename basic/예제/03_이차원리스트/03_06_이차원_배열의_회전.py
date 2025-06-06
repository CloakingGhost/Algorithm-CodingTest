# https://dailyalgo.kr/ko/problems/70

"""
            zip, -1     -1, -1      zip, -1, 1
13 15       3 15 13     13 3        15 7 13
15 7        13 7 15     7 15        13 15 3
3 13                    15 13


"""


def solution(numbers, rotate):
    if rotate == 90:
        return list(map(list, zip(*numbers[::-1])))  # 90도 회전
    elif rotate == 180:
        return [row[::-1] for row in numbers[::-1]]  # 180도 회전
    elif rotate == 270:
        return list(map(list, zip(*numbers)))[::-1]  # 270도 회전


print(solution([[13, 15], [15, 7], [3, 13]], 90))

print(
    solution(
        [
            [3, 13, 17, 14, 13],
            [1, 18, 16, 19, 7],
            [5, 6, 11, 15, 4],
            [14, 18, 15, 4, 18],
            [4, 16, 5, 15, 2],
        ],
        270,
    )
)

print(solution([[19, 8, 13]], 180))
