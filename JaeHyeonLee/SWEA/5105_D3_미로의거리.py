# region https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
"""
NxN 크기

최소 이동 수 
경로 없으면 0

0 통로
1 벽
2 시작
3 도착지

"""


# endregion

# 입력값 구조화
from collections import deque

T = int(input())

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for ts in range(1, T + 1):
    ans = float("inf")
    정점 = int(input())
    인접행렬 = [list(map(int, input())) for _ in range(정점)]

    예정지 = deque()
    방문지 = set()

    # 시작점 찾기
    for r in range(정점):
        for c in range(정점):
            if 인접행렬[r][c] == 2:
                예정지.append((r, c, -1))
                방문지.add((r, c))
                break
        if 예정지:
            break

    while 예정지:

        # 스택
        r, c, cnt = 예정지.pop()
        
        # 큐
        # r, c, cnt = 예정지.popleft()

        if 인접행렬[r][c] == 3:
            ans = min(ans, cnt)
            break

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if (
                0 <= nr < 정점
                and 0 <= nc < 정점
                and 인접행렬[r][c] != 1
                and (nr, nc) not in 방문지
            ):
                예정지.append((nr, nc, cnt + 1))
                방문지.add((nr, nc))

    # 도착 불가 시
    if ans == float("inf"):
        ans = 0
    print(f"#{ts} {ans}")
