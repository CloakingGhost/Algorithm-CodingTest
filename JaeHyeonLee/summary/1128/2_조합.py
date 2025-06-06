# region N과 M (5)
"""
정렬하여 순열
"""

# endregion

# region 풀이

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [0] * N
ans = []


def dfs(depth, idx):
    if depth == M:
        # print(' '.join(str(e) for e in ans))
        print(*ans)
        return
    for i in range(idx, N):
        if not visited[i]:
            ans.append(nums[i])
            visited[i] = 1
            dfs(depth + 1, i)

            ans.pop()
            visited[i] = 0


dfs(0, 0)
# endregion
