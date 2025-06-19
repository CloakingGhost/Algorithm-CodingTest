# https://www.acmicpc.net/problem/10971

import sys


input = sys.stdin.readline


def permutations(cost, depth, city):
    global min_cost
    if cost >= min_cost:
        return

    if depth == n - 1 and w[city][start_city] > 0:
        # 마지막이면 마지막 장소의 cost를 더해야 함
        min_cost = min(cost + w[city][start_city], min_cost)
        return

    for next_city in range(n):
        if not visited[next_city] and w[city][next_city] > 0:
            visited[next_city] = True
            # 과정 중의 cost는 여기서 더함
            permutations(cost + w[city][next_city], depth + 1, next_city)
            visited[next_city] = False


# 준비
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
min_cost = 1_000_000 * n
visited = [False] * (n + 1)

# 시작
visited[0] = True
cost, depth, start_city = 0, 0, 0
permutations(cost, depth, start_city)

# 결과
print(min_cost)
