# region

"""
행 depth
열 index
"""


# endregion

# region 풀이


def perm(depth, num):
    global ans
    if depth == N:
        ans = min(ans, num)
        return
      
      # 백트래킹
      # 가지치기
    if num >= ans:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            perm(depth + 1, num + matrix[depth][i])

            visited[i] = 0


T = int(input())
for ts in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = float("INF")

    perm(0, 0)

    print(f'#{ts} {ans}')


# endregion
