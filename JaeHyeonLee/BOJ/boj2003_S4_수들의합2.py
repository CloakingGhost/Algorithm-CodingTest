"""
4 2
1 1 1 1

3

10 5
1 2 3 4 2 5 3 1 1 2

3
"""

# region 투 포인터
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
l = r = ans = tmp = 0

while True:
    if tmp < M:
        if r < N:
            tmp += nums[r]
            r += 1
        else:
            break
    elif tmp > M:
        tmp -= nums[l]
        l += 1
    if tmp == M:
        ans += 1
        tmp -= nums[l]
        l += 1

print(ans)
# endregion
