# 시계 방향 90도 회전 (오른쪽으로 회전)
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

"""
[
    [9, 5, 1],
    [0, 6, 2],
    [1, 7, 3],
    [2, 8, 4]
]
"""
n = 3
m = 4

# 1. 행과 열의 크기를 바꾼 새로운 이차원 리스트를 초기화 => 모든 원소를 0으로 초기화
rotated_matrix = []
for _ in range(m):
    line = [0] * n  # 새로운 행을 초기화
    rotated_matrix.append(line)

rotated_matrix = [[0] * n for _ in range(m)]
print(rotated_matrix)

# 2. 반복문을 돌면서 새로운 이차원 리스트를 채워나간다.
## 회전 기준을 정해야 함

for i in range(m):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n - 1 - j][i]  # 끝에서 하나씩 빼준다.

print(rotated_matrix)

# 내장함수 zip()을 이용한 90도 회전
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

## 일단 zip()에 대해 알아보자
### 동일한 인덱스의 원소를 모은다
a = zip([1, 2], [3, 4], [5, 6])  # (1, 3, 5), (2, 4, 6)
print(list(a))

## 이제 zip을 이용하여 회전해보자
### 튜플의 원소가 1개인 경우 => (1,)
### 이차원 리스트의 각 행을 zip()에 넣으면 각 행이 튜플로 묶인다.
#### 각 인덱스에 있는 리스트의 원소들이 같은 인덱스이기 때문
print(list(zip(matrix)))  # [([1, 2, 3, 4],), ([5, 6, 7, 8],), ([9, 0, 1, 2],)]
print(list(zip(*matrix)))  # 언팩킹
print(list(zip(*matrix[::-1])))

# rotated_matrix = list(zip(*matrix[::-1]))  # 역순으로 회전
rotated_matrix = list(map(list, zip(*matrix[::-1])))  # 리스트로 변환

print(rotated_matrix)
