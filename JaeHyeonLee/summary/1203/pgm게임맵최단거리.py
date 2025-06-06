maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
]
from collections import deque


def solution(maps):
    # 초기 세팅(출발지, 예정지, 기록지)
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    N = len(maps[0])  # c
    M = len(maps)  # r
    padding_maps = [[0] * (N+2) for _ in range(M+2)]
    for i in range(1, M + 1):
        padding_maps[i][1:N+1] = maps[i-1]
    visited = [[0] * N for _ in range(M)]
    queue = deque([(0, 0, 1)])
    ans = -1
    
    # 예정지가 빌 때까지
    while queue:
        # 방문
        r, c, cnt = queue.popleft()
        if r == M - 1 and c == N - 1:
            ans = cnt
        # 탐색
        for d in range(4):
            # 좌표 찍고
            nr, nc = r + dr[d], c + dc[d]
            # 갈 수 있다면
            if (
                # 0 <= nr < M
                # and 0 <= nc < N and 
                
                not visited[nr][nc]
                and maps[nr][nc] == 1
            ):
                # 방문 체크
                visited[nr][nc] = 1
                # 예정지에 넣기
                queue.append((nr, nc, cnt + 1))
    return ans


print(solution(maps))
