# https://www.acmicpc.net/problem/20364

import sys

input = sys.stdin.readline
n, q = map(int, input().split())

tree = [False] * (n + 1)
for _ in range(q):
    target = int(input())
    parent = target
    answer = 0
    while parent > 0:
        if tree[parent]:
            answer = parent

        parent = parent // 2  # 완전 이진 트리의 특성

    if answer == 0:  # 방문한 곳에 갔으면 값이 달라짐
        tree[target] = True

    print(answer)
