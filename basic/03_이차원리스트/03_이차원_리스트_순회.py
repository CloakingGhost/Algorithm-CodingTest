# 1. 행 우선 순회(행순회)
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
"""
다음과 같이 출력하여라.
1 2 3 4
5 6 7 8
9 0 1 2
"""
for i in range(3):
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()

# 2. 열 우선 순회(열순회)
"""
다음과 같이 출력하여라
1 5 9
2 6 0
3 7 1
4 8 2
"""

for i in range(4):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()
