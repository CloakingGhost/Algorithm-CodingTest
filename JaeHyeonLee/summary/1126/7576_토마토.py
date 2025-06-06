# region 7576 양 BFS

import sys
input = sys.stdin.readline
from collections import deque

# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 세팅(출발지, 기록지, 예정지)
visited = set()
queue = deque()

for r in range(N):
  for c in range(M):
    if box[r][c] == 1:
      queue.append((r, c, 0))

# 예정지가 빌 때까지
while queue:
  # 방문
  r, c, cnt = queue.popleft()
  # 탐색 - 델타 탐색
  # 네 방향을 확인하며
  for d in range(4):
    # 새로운 좌표를 찍어보고
    nr, nc = r + dr[d], c + dc[d]
    # 유효한지 확인하고(범위, 안익은 토마토 인지(0이고 방문X))
    # if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0 and (nr, nc) not in visited:
    if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0 :
      # 방문체크하고 | 원본배열 변환
      # visited.add((nr, nc))
      box[nr][nc] = 1
      # 큐에 넣기 | cnt += 1으로 거리값 
      queue.append((nr, nc, cnt + 1))
      

      
# 다 익었는지 확인
for row in box:
  if 0 in row:
    cnt = -1
    break
# 다 익었다면 얼마나 걸렸는지 확인

print(cnt)
# endregion

#region



import sys
input = sys.stdin.readline
from collections import deque

# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 세팅(출발지, 기록지, 예정지)
visited = set()
queue = deque()

for r in range(N):
  for c in range(M):
    if box[r][c] == 1:
      queue.append((r, c))

# 예정지가 빌 때까지
while queue:
  # 방문
  r, c, cnt = queue.popleft()
  # 탐색 - 델타 탐색
  # 네 방향을 확인하며
  for d in range(4):
    # 새로운 좌표를 찍어보고
    nr, nc = r + dr[d], c + dc[d]
    # 유효한지 확인하고(범위, 안익은 토마토 인지(0이고 방문X))
    # if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0 and (nr, nc) not in visited:
    if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0 :
      # 방문체크하고 | 원본배열 변환
      # visited.add((nr, nc))
      box[nr][nc] = box[r][c] + 1
      # 큐에 넣기 | cnt += 1으로 거리값 
      queue.append((nr, nc))
      

      
# 다 익었는지 확인
cnt = 0
for row in box:
  if 0 in row:
    cnt = 0
    break
  cnt = max(cnt, *row)
# 다 익었다면 얼마나 걸렸는지 확인

print(cnt - 1)


#endregion