# https://www.acmicpc.net/problem/10773

import sys

input = sys.stdin.readline

k = int(input())

stack = []

for _ in range(k):
    element = int(input())
    if element == 0:
        if stack:
            stack.pop()
        else:
            stack.append(element)
    else:
        stack.append(element)
print(sum(stack))
