# 이차원 리스트의 총합
matrix = [[0, 5, 3, 1], [4, 6, 10, 8], [9, -1, 1, 5]]

total = 0
for i in range(3):
    for j in range(4):
        total += matrix[i][j]
print("총합:", total)

## 내장함수 sum()을 이용한 총합
total = 0

for i in range(3):
    total += sum(matrix[i])

for line in matrix:
    total += sum(line)

print("총합:", total)

## pythonic한 총합
total = 0

for line in matrix:
    total += sum(line)

print("총합:", total)
