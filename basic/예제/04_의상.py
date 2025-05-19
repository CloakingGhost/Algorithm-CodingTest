# https://school.programmers.co.kr/learn/courses/30/lessons/42578


from collections import Counter


def solution(clothes):
    category_counter = Counter(category for name, category in clothes)
    counter_values = category_counter.values()
    answer = 1
    for value in list(counter_values):
        answer *= value + 1
    return answer - 1


print(
    solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)
