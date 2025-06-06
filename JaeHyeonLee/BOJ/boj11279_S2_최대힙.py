# region 문제정리
"""
자연수 x 넣기
큰 값 출력 후 제거




# 연산 횟수: N

# N 만큼 반복
  # 입력값 x
  
  # 자연수면 배열에 추가
  # 0 이면 
    # 배열 비었으면 0
    # 있으면 출력 후 삭제
"""


# endregion


# region 풀이
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
# 연산 횟수: N
N = int(input())

# heap 배열
heap = []
# N 만큼 반복
for _ in range(N):
    # 입력값 x
    x = int(input())
    # 자연수면
    if x:
        # 배열에 추가
        heappush(heap, -x)
    # 0 이면
    else:
        # 배열 비었으면 0
        if not heap:
            print(0)
        # 있으면 출력 후 삭제
        else:
            print(-heappop(heap))


# endregion
