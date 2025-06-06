# region https://www.acmicpc.net/problem/2164
"""

1 ~ N 까지
한 장 남을 때까지 반복

1. 제일 위 바닥에 버림
2. 제일 위에 있는 카드를 제일 아래로


"""

# endregion

import sys
from collections import deque

input = sys.stdin.readline
nums = deque([n for n in range(int(input()))])
while len(nums) != 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums.pop() + 1)
