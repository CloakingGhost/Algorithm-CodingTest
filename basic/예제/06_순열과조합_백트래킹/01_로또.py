# https://www.acmicpc.net/problem/6603
# 조합

import sys

# 상수
lottery_length = 6


def combinations(current, start):
    if len(current) == lottery_length:
        answer.append(current[:])
        return

    for i in range(start, k):
        current.append(numbers[i])
        combinations(current, i + 1)
        current.pop()


input = sys.stdin.readline
while True:
    answer = []
    ts = list(map(int, input().split()))
    k, *numbers = ts
    if k == 0:
        break

    combinations([], 0)
    for row in answer:
        print(*row)
    print()

"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

7 1 2 3 4 5 6 7
0

"""

from itertools import combinations
import sys

# 상수
lottery_length = 6

input = sys.stdin.readline

while True:
    answer = []
    ts = list(map(int, input().split()))
    k, *numbers = ts
    if k == 0:
        break

    for row in combinations(numbers, lottery_length):
        print(*row)
    print()
