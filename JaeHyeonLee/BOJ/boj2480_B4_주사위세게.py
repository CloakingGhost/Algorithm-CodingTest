# region 문제 정리
"""

1 ~ 6까지 주사위 3개

1. 같은 수 3개 => 10_000 + 수 * 1_000
2. 같은 수 2개 => 1_000 + 수 * 100
3. 다 다르면 => 가장 큰 수 * 100

###############

문자 3개 받아서 숫자 배열로 만듬
정렬

if 배열[0] == 배열[2]:
  1. 같은 수 3개 => 10_000 + 수 * 1_000
elif 배열[0] == 배열[1]:
  2. 같은 수 2개 => 1_000 + 수 * 100
elif 배열[1] == 배열[2]
  2. 같은 수 2개 => 1_000 + 수 * 100
else
  3. 다 다르면 => 가장 큰 수 * 100

"""


# endregion


# region 풀이
import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))
nums.sort()
if nums[0] == nums[2]:
    print(10_000 + nums[0] * 1_000)
elif nums[0] == nums[1] or nums[1] == nums[2]:
    print(1_000 + nums[1] * 100)
else:
    print(nums[2] * 100)

# endregion
