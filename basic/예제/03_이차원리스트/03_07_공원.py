def solution(mats, park):
    mats.sort(reverse=True)
    for mat in mats:
        for i in range(len(park) - mat + 1):
            for j in range(len(park[0]) - mat + 1):
                # 모두 -1인지 확인
                if all(
                    park[i + x][j + y] == "-1" for y in range(mat) for x in range(mat)
                ):
                    return mat
    return -1


print(
    solution(
        [5, 3, 2],
        [
            ["A", "A", "-1", "B", "B", "B", "B", "-1"],
            ["A", "A", "-1", "B", "B", "B", "B", "-1"],
            ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
            ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
            ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
            ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
        ],
    )
)
