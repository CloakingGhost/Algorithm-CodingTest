# # region
# """
# 가중치가 들어간 인접행렬
# 문제에 주어진 입력값이 구조화 되어 있으므로
# 문제만 풀면됨

# 마지막에서 출발지로 가는 경로 + 1

# 0에서 출발하는 순환 경로 모두 탐색
# 순환이기 때문에 중복됨
# """

# # endregion

# # region 풀이

# N = int(input())
# adj_matrix = [list(map(int, input().split())) for _ in range(N)]


# def perm(now, depth, cost):
#     # 마지막 도시에 도착하면(depth == N)
#     if depth == N:
#         # 마지막 - 출발 가는 비용을 더해주고
#         # cost += adj_matrix[now][0]
#         # 정답 갱신 하고 리턴
#         ans = min(ans, cost)
#         return
#     if cost >= ans:
#         return

#     # 갈 수 있는 곳을 탐색하여
#     for after in range(N):
#         # 방문한적 없고, 0이 아니라면
#         if not visited[after] and adj_matrix[now][after]:
#             print(f'{now} : {after} // {adj_matrix[now][after]}')
#             # 방문 체크하고
#             visited[after] = 1
#             # 방문(재귀)
#             perm(after, depth + 1, cost + adj_matrix[now][after])
#             # 방문 체크 해제
#             visited[after] = 0


# # 세팅(출발지, 예정지, 도착지)
# # dfs 예정지 없어도 됨
# visited = [0] * N
# ans = float("INF")

# visited[0] = 1
# perm(0, 1, 0)


# # endregion


import sys

input = sys.stdin.readline


def dfs(now, cost, depth):
    global ans

    if depth == N:
        if cost_matrix[now][0]:
            cost += cost_matrix[now][0]
            ans = min(ans, cost)
            return
        else:
            return

    if cost > ans:
        return

    for after in range(N):
        print(f"before // {now} : {after} , depth : {depth}")
        if not check[after] and cost_matrix[now][after]:
            print(f"{now} : {after} // {cost_matrix[now][after]}")
            check[after] = 1
            dfs(after, cost + cost_matrix[now][after], depth + 1)
            check[after] = 0
            print()


N = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(N)]

check = [0] * N
ans = 987654321

check[0] = 1
dfs(0, 0, 1)

print(ans)
