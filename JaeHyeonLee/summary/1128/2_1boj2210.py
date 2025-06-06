# region 문제 정리
"""

"""

# endregion

# region 풀이
matrix = [list(input().split()) for _ in range(5)]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
ans = set()

# visited = set() # 이 문제는 필요없음 visited.discard(el)


def perm(depth, r, c, num):
    if depth == 5:
        # 집합에 집어넣고 리턴
        ans.add(num)
        return
    # 다음에 갈 곳을 탐색해서(델타 탐색)
    for d in range(4):
      # 다음 좌표 찍어보고
        nr, nc = r + dr[d], c + dc[d]
        # 유효성 검사 후에(범위)
        if 0 <= nr < 5 and 0 <= nc < 5:
            # 재귀
            perm(depth + 1, nr, nc, num + matrix[nr][nc])


# 순회 하면서
# 모든 칸에서 DFS/prem
for i in range(5):
    for j in range(5):
        perm(0, i, j, matrix[i][j])

print(len(ans))

# endregion








