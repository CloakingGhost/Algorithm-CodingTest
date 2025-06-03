# https://www.acmicpc.net/problem/2563

# 점을 찍어 전부 더하기
import sys

input = sys.stdin.readline
n = int(input())

board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

print(sum(map(sum, board)))
