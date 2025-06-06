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
def dfs(depth):
  if depth == M:
    # print(' '.join(str(e) for e in ans))
    print(*ans)
    return
  for idx in range(N):
    if not visited[idx]:
      ans.append(nums[idx])
      visited[idx] = 1
      dfs(depth+1)
      
      ans.pop()
      visited[idx] = 0

dfs(0)
# endregion
