# region 문제 정리
"""
피보나치 구현
"""

# endregion
# region 풀이

n = int(input())

cnt = 0
n1, n2 = 0, 1
while cnt <= n:
  n3 = n1 + n2
  n1, n2, n3 = n2, n3, n1
  cnt += 1
print(n3)
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(n))
# endregion
# region 알게 된점


# endregion
