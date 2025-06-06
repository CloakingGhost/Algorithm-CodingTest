# region 문제 정리

"""
최소 힙 사용
배열에 x 넣기
배열에서 가장 작은 값 출력 후 제거


# 연산의 개수(반복 횟수)

# N 만큼 반복
  # 입력값 받기
  
  # 만약 빈 배열이면
    # 0 출력
  # 입력값이 자연수 라면
    # heappush
  # 입력값이 0이면
    # 출력 후 제거, heappop
  
"""
# endregion

# region 풀이

from heapq import heappop, heappush
import sys
input=sys.stdin.readline

# 연산의 개수(반복 횟수)
N = int(input())

heap = []
# N 만큼 반복
for _ in range(N):
    # 입력값 받기
    x = int(input())
    # 입력값이 0이면
    if x == 0:
        # 빈 배열이면
        if len(heap) == 0:
            # 0 출력
            print(0)
            continue
        # 출력 후 제거, heappop
        print(heappop(heap))
    # 입력값이 자연수 라면
    else:
        # heappush
        heappush(heap, x)


# endregion

# region ver2

from heapq import heappop, heappush
import sys
input=sys.stdin.readline

N = int(input())

heap = []
# N 만큼 반복
for _ in range(N):
    # 입력값 받기
    x = int(input())
    # 입력값이 0이면
    if not x:
        # 빈 배열이면
        if not heap:
            # 0 출력
            print(0)
        # 아니면 출력 후 제거, heappop
        else :
          print(heappop(heap))
    # 입력값이 자연수 라면
    else:
        # heappush
        heappush(heap, x)


# endregion