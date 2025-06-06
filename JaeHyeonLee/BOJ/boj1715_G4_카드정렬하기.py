# region 문제 정리
"""
      100번
          70번
    30번    
10개    20개    40개
          60번
    70번
        130번
#############

10개    20개    40개

10 + 40 = 50번
50 + 20 = 70번

50번 + 70번 = 120번
#############

최소값으로 비교할 때 비교횟수가 적음
두 뭉치씩 고금
"""

# endregion

# region 풀이
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

# 카드 묶음 개수
N = int(input())
heap = []
ans = 0

# 입력값 받기
for _ in range(N):
    heappush(heap, int(input()))

# 반복: 2개를 뽑으니까 1개가 될때까지
while len(heap) > 1:
    # 가장 작은 값 2개 추출
    c1, c2 = heappop(heap), heappop(heap)
    # 합한다
    c = c1 + c2
    # 비교하는 횟수 갱신(정답변수)
    ans += c
    # 합한 카드 heap에 넣는다
    heappush(heap, c)

# 정답 출력
print(ans)
# endregion
