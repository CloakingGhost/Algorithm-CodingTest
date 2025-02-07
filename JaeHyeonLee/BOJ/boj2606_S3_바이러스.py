# region https://www.acmicpc.net/problem/2606
"""
0번은 사용하지 않음
1번 정점부터 연결된 정점을 찾는 문제
"""

# endregion

import sys
from collections import deque
input = sys.stdin.readline

정점 = int(input())
간선 = int(input())

# 구조화 (양방향)

인접리스트 = [[] for _ in range(정점+1)]

for _ in range(간선):
  시작점, 끝점 = map(int, input().split())
  인접리스트[시작점].append(끝점)
  인접리스트[끝점].append(시작점)

예정지 = deque([1])
방문지 = {1}
while 예정지:
  현재_정점 = 예정지.pop()
  
  for 다음_정점 in 인접리스트[현재_정점]:
    if 다음_정점 not in 방문지:
      예정지.append(다음_정점)
      방문지.add(다음_정점) 
      
print(len(방문지) - 1) # 시작점 제외
      
    


