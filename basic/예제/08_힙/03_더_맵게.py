from heapq import heappop, heappush, heapify


def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville[0] < K and len(scoville) >= 2:
        food_1, food_2 = heappop(scoville), heappop(scoville)
        heappush(scoville, food_1 + (food_2 * 2))
        answer += 1

    if scoville[0] < K:
        return -1

    return answer


print(solution([12, 9, 3, 2, 10, 1], 1000))
