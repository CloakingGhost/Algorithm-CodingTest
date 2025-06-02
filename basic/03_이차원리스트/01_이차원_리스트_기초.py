# 이차원리스트의 조회와 수정
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][0])  # 1
print(matrix[2][2])  # 9

matrix[0][0] = 10  # 1 -> 10
print(matrix[0][0])  # 10

# 이차원 리스트의 초기화

matrix = []

for _ in range(3):  # 행
    matrix.append([0] * 4)  # 열

print(matrix)

matrix = [[0] * 4 for _ in range(3)]  # 깊은 복사
print(matrix)

matrix = [[0] * 4] * 3  # 얕은 복사 발생
# [0] * 4는 얕은 복사,
# 변경할 때는 바라보는 원본값은 immutable 함으로
# 새로운 객체를 생성하고 그 객체를 바라 봄.
