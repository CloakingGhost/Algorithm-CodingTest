# https://www.acmicpc.net/problem/9012
# 괄호 문자열(Parenthesis String, PS)

"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

1
(()())((()))
"""

import sys
from collections import deque

input = sys.stdin.readline


def isVPS(ps):
    stack = deque()
    for elem in ps:
        if elem == "(":
            stack.append(elem)
            continue
        if not stack:
            return "NO"
        stack.pop()

    return "NO" if stack else "YES"


t = int(input())
print(*[isVPS(input().rstrip()) for _ in range(t)], sep="\n")
