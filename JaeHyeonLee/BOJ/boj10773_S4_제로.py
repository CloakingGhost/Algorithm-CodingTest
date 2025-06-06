# region https://www.acmicpc.net/problem/10773

"""
하나씩 받고 숫자로 변경
배열이 비었으면 0
있으면 sum(배열)

"""
# endregion

import sys
from collections import deque

input = sys.stdin.readline

stack = deque()

for _ in range(int(input())):
  num = int(input())
  if num :
    stack.append(num)
  else :
    stack.pop()
    
print(sum(stack))