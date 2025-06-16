# 조합(Combinations) : 순서가 "없게" 뽑는 경우의 수
## 방문배열 없어도 됨


# 1. 재귀
# current - 현재 내가 뽑은 숫자들
# start - 내가 다음 숫자를 어디서부터 뽑을지에 대한 인덱스
def combinations(current, start):
    ## 1. 종료조건
    if len(current) == length:
        result.append(current[:])
        return
    ## 2. 재귀식

    for i in range(start, len(numbers)):
        current.append(numbers[i])
        combinations(current, i + 1)  # i를 다시 방문하지 않아도 됨
        current.pop()


numbers = [1, 2, 3, 4]
length = 3
result = []

combinations([], 0)
# print(*result, sep="\n")

# 2. 모듈
from itertools import combinations

numbers = [1, 2, 3, 4]
length = 3

print(*combinations(numbers, length), sep="\n")
