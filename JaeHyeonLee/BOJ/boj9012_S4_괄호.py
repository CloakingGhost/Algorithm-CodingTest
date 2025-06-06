# region https://www.acmicpc.net/problem/9012
"""
스택을 사용하여 괄호의 짝이 맞는지 확인하는 문제

"""

# endregion

# region 구현

import sys

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    ans = "YES"
    stack = []
    round_brackets = list(input().rstrip())
    for rb in round_brackets:
        if rb == "(":
            stack.append(rb)
        else:
            if stack:
                stack.pop()
            else:
                ans = "NO"
                break
    if stack:
        ans = "NO"

    print(ans)
