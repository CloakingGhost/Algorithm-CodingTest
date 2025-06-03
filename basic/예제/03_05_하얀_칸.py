# https://www.acmicpc.net/problem/1100

import sys

input = sys.stdin.readline

n = 8  # 체스판의 크기, 정사각형
answer = 0
# 입력
board = [input().rstrip() for _ in range(n)]
count = 0
# 풀이
for i in range(n):
    # isOddRow = i % 2 == 1  # 홀수 행
    for j in range(n):
        count += 1
        if (i + j) % 2 and board[i][j] == "F":
            answer += 1
# 출력
# print(answer)
print(count)
