# region 정렬

"""
불안정 정렬보다
안정 정렬이 우월하다


시간순으로 정렬 했는데
지역순으로 다시 정렬했을 경우
시간에 대한 정렬의 순서가 변하는건 옳지 않다
때문에 안정정렬이 우월하다

"""

# endregion

# region 2차원 배열
matrix = [[3, 7, 9], [4, 2, 6], [8, 1, 5]]


# 순회
for r in range(3):
    for c in range(3):
        print(matrix[r][c])

for c in range(3):
    for r in range(3):
        print(matrix[r][c])


# 전치 for
for r in range(2):
    for c in range(r + 1, 3):
        matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

for r in range(3):
    print(matrix[r])
# 전치 zip
# 가장 짧은 행 길이 만큼 열을 데이터로 튜플을 만든다
print(zip(*matrix))
print(list(map(list, zip(*matrix))))

# endregion


# region 델타 탐색
"""
내가 지금 있는 곳을 기준으로 주변을 순회
"""
# 델타 : 방향
#     상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

matrix = [[3, 7, 9], [4, 2, 6], [8, 1, 5]]


r, c = 2, 2

for d in range(4):
  nr, nc = r + dr[d], c + dc[d]
  print(matrix[nr][nc])
  # r, c = nr, nc # 이동

# endregion
