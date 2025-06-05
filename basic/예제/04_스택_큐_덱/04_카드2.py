# https://www.acmicpc.net/problem/2164

import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
stack = deque([i + 1 for i in range(n)])

while len(stack) > 1:
    stack.popleft()
    if stack:
        stack.append(stack.popleft())

print(stack[-1])
