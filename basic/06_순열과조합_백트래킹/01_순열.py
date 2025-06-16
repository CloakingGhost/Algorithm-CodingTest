# 순열(Permutation) -> 순서가 "있게" 뽑는 경우의 수
# 1. 반복문
numbers = [1, 2, 3, 4]

## 3개를 뽑아보자(3개의 반복문)
result = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            if i != j and j != k and k != i:
                result.append([numbers[i], numbers[j], numbers[k]])
# print(*result, sep="\n")


# 2. 재귀
## 추가 조건이 있을 경우
def permutations(current):
    # 1. 종료조건
    if len(current) == length:
        # result.append(current) # 할당, 동일 객체를 가리키고 있음
        result.append(current[:])  # 얕은 복사
        return

    # 2. 점화식(재귀식)
    for i in range(len(numbers)):
        if not visited[i]:
            ## 1. i번째 원소 뽑기
            visited[i] = True
            current.append(numbers[i])

            ## 2. 다음 원소를 뽑기 위해 재귀식 진행
            permutations(current)

            ## 3. 재귀식 종료 후, 뽑았던 i번째 원소 제거
            visited[i] = False
            current.pop()


numbers = [1, 2, 3, 4]
length = 3  # 뽑고 싶은 개수
visited = [False] * len(numbers)
result = []

permutations([])
# print(*result, sep="\n")

# 3.모듈(라이브러리)
## 효율성, 시간복잡도 문제
from itertools import permutations

대상 = [1, 2, 3, 4]
뽑을_개수 = 3

print(*permutations(대상, 뽑을_개수), sep="\n")
