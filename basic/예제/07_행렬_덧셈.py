# https://www.acmicpc.net/problem/2738
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a_matrix = []
for _ in range(n):
    a_matrix.append(list(map(int, input().split())))

for i in range(n):
    b_row = list(map(int, input().split()))
    for j in range(m):
        a_matrix[i][j] += b_row[j]

for row in a_matrix:
    print(*row)
