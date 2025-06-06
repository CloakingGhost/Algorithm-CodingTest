# https://school.programmers.co.kr/learn/courses/30/lessons/43165


def solution(numbers, target):
    def dfs(depth, total):
        if depth == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1

            return
        dfs(depth + 1, total + numbers[depth])
        dfs(depth + 1, total - numbers[depth])

    answer = 0
    dfs(0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))
