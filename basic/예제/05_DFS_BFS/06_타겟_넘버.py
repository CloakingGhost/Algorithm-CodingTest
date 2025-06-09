# https://school.programmers.co.kr/learn/courses/30/lessons/43165

<<<<<<< HEAD
# region

=======
<<<<<<< HEAD
# region

=======
>>>>>>> main
>>>>>>> main

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


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
# endregion


def solution(numbers, target):
    answer = 0

    def dfs(depth, total):
        if depth == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1
            return
        dfs(depth + 1, total + numbers[depth])
        dfs(depth + 1, total - numbers[depth])

    dfs(0, 0)
    return answer


from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])
    while queue:
        depth, total = queue.popleft()
        if depth == len(numbers):
            if total == target:
                answer += 1
            continue

        queue.append((depth + 1, total + numbers[depth]))
        queue.append((depth + 1, total - numbers[depth]))
    return answer


<<<<<<< HEAD
=======
=======
>>>>>>> main
>>>>>>> main
print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))
