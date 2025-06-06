import sys

input = sys.stdin.readline

## 입력
n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]

## 합하기
for i in range(n):
    for j in range(m):
        matrix1[i][j] += matrix2[i][j]

## 출력
for i in range(n):
    for j in range(m):
        print(matrix1[i][j], end=" ")
    print()

# for line in matrix1:
#     print(*line)  # unpacking을 이용하여 출력
