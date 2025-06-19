# https://dailyalgo.kr/ko/problems/61
# 조합


def solution(volume, items):
    def combinations(weight, value, start):
        nonlocal answer

        for i in range(start, len(items)):
            x, y = items[i]
            if weight + x <= volume:
                combinations(weight + x, value + y, i + 1)
                answer = max(answer, value + y)

    answer = 0
    combinations(0, 0, 0)
    return answer


print(solution(5, [[4, 1], [1, 3]]))
print(solution(23, [[4, 1], [9, 3], [10, 10], [9, 8], [5, 9]]))
print(solution(20, [[4, 9], [3, 3]]))
print(solution(3, [[4, 6], [10, 10]]))
