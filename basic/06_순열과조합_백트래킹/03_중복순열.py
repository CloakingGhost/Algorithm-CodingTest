# 중복순열(Product)
## 뽑은 것을 한번 더 뽑음
### 122, 111, 333 등

# 1. 재귀


def product(current):
    # 1. 종료조건
    if len(current) == length:
        result.append(current[:])
        return

    # 2. 재귀식
    ## 방문한 곳을 반복해서
    ## 방문이 가능하므로 visited 없어도 됨
    ## 모든 경우 탐색
    # for i in range(len(numbers)):
    #     current.append(numbers[i])
    #     product(current)
    #     current.pop()
    for number in numbers:
        current.append(number)
        product(current)
        current.pop()


numbers = [1, 2, 3, 4]
length = 3
result = []

product([])

# print(*result, sep="\n")
# 2.모듈
from itertools import product

numbers = [1, 2, 3, 4]
length = 3
print(*product(numbers, repeat=length), sep="\n")
