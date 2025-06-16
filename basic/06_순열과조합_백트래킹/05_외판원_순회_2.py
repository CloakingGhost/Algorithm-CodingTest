# https://www.acmicpc.net/problem/10971

import sys


input = sys.stdin.readline


# 방문한 곳은 가지 않을 것이기 때문에
# 방문횟수로 몇 곳을 방문했는지 확인
# city : 현재 내가 몇  번재 도시인지에 대한 도시 번호
# depth :  현재 내가 몇 개의 도시를 탐색했는지 그 깊이
# cost : 현재 도시까지 왔을 대의 총 비용
def permutations(city, depth, cost):
    global min_cost

    # 백트래킹(Back-Tracking): 유망성이 없어 이전으로 되돌아감
    if cost >= min_cost:
        return

    # 1. 종료조건
    if (
        # 출발 노드로 돌아오기 직전인지
        depth == n - 1
        # 출발 노드로 갈 수 있는지
        and w[city][0] > 0
    ):
        min_cost = min(min_cost, cost + w[city][0])
        return

    # 2. 재귀식
    for next_city in range(n):
        if not visited[next_city] and w[city][next_city] > 0:
            visited[next_city] = True
            permutations(next_city, depth + 1, cost + w[city][next_city])
            visited[next_city] = False


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]  # 인접행렬
visited = [False] * n
min_cost = 10_000_000  # 문제의 최대값

# 임의의 점 한 곳만 확인하면 정답 찾음
# 시작 순서만 다를 뿐 비용의 합은 동일하기 때문
visited[0] = True
permutations(0, 0, 0)  # city, depth, cost

print(min_cost)
