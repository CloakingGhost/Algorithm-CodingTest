# https://dailyalgo.kr/ko/problems/79


def sort_key(unit):
    return (unit[0], abs(unit[1]))


def solution(numbers):
    numbers.sort(key=sort_key)
    return numbers


# [[1,7],[2,-5],[3,-1],[3,4]]
print(solution([[3, 4], [2, -5], [3, -1], [1, 7]]))
# [[-1,2],[-1,-3],[0,-4],[0,5]]
print(solution([[-1, 2], [-1, -3], [0, 5], [0, -4]]))
# [[2,1],[3,2],[5,-6],[5,6]]
print(solution([[5, -6], [3, 2], [5, 6], [2, 1]]))
