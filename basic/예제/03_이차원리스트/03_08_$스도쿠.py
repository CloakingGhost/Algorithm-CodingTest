# https://www.acmicpc.net/problem/9291

import sys

input = sys.stdin.readline
T = int(input())

for tc in range(T):
    sudoku = [list(input().split()) for _ in range(9)]
    flag = True
    reversed_sudoku = list(map(list, zip(*sudoku)))
    for i in range(9):
        if (len(set(sudoku[i])) + len(set(reversed_sudoku[i]))) != 18:
            flag = False
            break

        # 012 345 678
    if flag:
        for i in range(0, 9, 3):  # (0, 3, 6)
            for j in range(0, 9, 3):
                sets = set(sudoku[i + k][j + l] for k in range(3) for l in range(3))
                if len(sets) != 9:
                    flag = False
                    break
            if not flag:
                break

    print(f"Case {tc + 1}: {"CORRECT" if flag else "INCORRECT"}")
    if tc < T - 1:
        input()  # 빈 줄을 읽어들임
