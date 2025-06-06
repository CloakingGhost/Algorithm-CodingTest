# region BFS
from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())


# 세팅(출발지, 예정지, 기록지)
queue = deque([(N, 0)])
visited = set([N])

# BFS
while queue:
  # 방문
    cur, time = queue.popleft()
    
    # K에 도착했는지 확인 
    if cur == K:
        break
      
    #탐색
    for nxt in [cur + 1, cur - 1, cur * 2]:
        if 0 <= nxt <= 140_000 and nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, time + 1))

            # queue.append((cur + 1, time + 1))
            # visited.add(cur + 1)
            # queue.append((cur - 1, time + 1))
            # visited.add(cur - 1)
            # queue.append((cur * 2, time + 1))
            # visited.add(cur * 2)


print(time)
# endregion
