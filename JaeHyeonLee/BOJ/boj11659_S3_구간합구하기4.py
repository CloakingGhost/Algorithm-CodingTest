# region 문제 정리
"""
입력
N : 주어지는 수의 개수
M : 목표 값의 횟수(반복의 횟수)
i, j : i 부터 j 까지의 합(인덱스 아님)

출력
i 부터 j 까지의 합


누적합

누적합 배열
반복문을 돌며
  누적합을 계산
  값 출력
"""


# endregion
# region 풀이

import sys

input = sys.stdin.readline


N, M = map(int, input().split())
lst = list(map(int, input().split()))
acc_lst = [0]
for i in range(N):
    acc_lst.append(acc_lst[-1] + lst[i])


for _ in range(M):
    start, end = map(int, input().split())
    print(acc_lst[end] - acc_lst[start - 1])

# endregion

# region 깨달은 점
"""
그림을 그리면 어느 인덱스에 -1을 해야하는지 빠르게 파악가능
"""


# endregion
