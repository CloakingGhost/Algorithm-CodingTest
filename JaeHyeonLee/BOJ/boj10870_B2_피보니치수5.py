# region 문제 정리
"""
n번째 피보나치 수 

피보나치수
0, 1로 시작하여 두 수를 더한 값에 직전 값을 누적하여 더한다

n이 될 때까지 반복하여 0 1로 누적하여 더한다

"""

# endregion

# region 풀이
n = int(input())
n1, n2 = 0, 1

cnt = 0
while cnt <= n:
  n3 = n1 + n2
  n1, n2, n3 = n2, n3, n1
  cnt += 1
print(n3)


def fibo(N):
    if N <= 1:
        return N
    return fibo(N - 1) + fibo(N - 2)


print(fibo(n))

# endregion

# region 알게 된 점
'''
while을 사용하면 뭔가 복잡하다

재귀를 사용하면 시작값까지 내려갔다가 찾은 시작 값부터 다시 오라오면서 계산
시작값은 재귀 함수의 조건에 들어가게 됨
'''

# endregion
