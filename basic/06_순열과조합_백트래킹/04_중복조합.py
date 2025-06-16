# 중복조합(combinations with replacement)


# 1. 재귀
def combinations_with_replacement(current, start):
    ## 1. 종료조건
    if len(current) == length:
        result.append(current[:])
        return

    # 2. 재귀식
    for i in range(start, len(numbers)):
        current.append(numbers[i])
        combinations_with_replacement(current, i)  # 시작 지점을 다시 전달
        current.pop()


numbers = [1, 2, 3, 4]
length = 3
result = []

combinations_with_replacement([], 0)
# print(*result, sep="\n")

# 2. 모듈
from itertools import combinations_with_replacement

numbers = [1, 2, 3, 4]
length = 3
print(*combinations_with_replacement(numbers, length), sep="\n")
