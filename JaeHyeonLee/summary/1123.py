# region 재귀 탬플릿

# 1. 빈 판 만들기

# 2. 간선정보 입력받기
#######################

# 세팅(출발지, 예정지, 기록지)
# 재귀를 사용하면 예정지를 만들지 않아도 된다
# 스택과 아주아주 유사하다, 사실상 시스템 스택

# 1번 로직 + 재귀함수 + 2번 로직
# 1번 로직을 만나고 함수를 호출하면 2번로직은 리턴 되었을 때 시행되기 때문

# 방문

# 탐색

# endregion
# region boj2606 바이러스 재귀


V = int(input())
E = int(input())

# 1. 빈 판 만들기
adj_lst = [[] for _ in range(V + 1)]

# 2. 간선정보 입력받기
for _ in range(E):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)


######################

# 세팅(출발지, 예정지, 기록지)
visited = [0] * (V + 1)  # 비트마스킹(0, 1로 이루어져 있음) 0, 1에 의미를 부여하면 됨
visited[1] = 1


# start(cur): 정점 번호
def DFS(cur):

    # 방문: 함수에 들어오는 순간 방문

    # 탐색
    # cur에서 갈 수 잇는 곳 중에서
    for nxt in adj_lst[cur]:
        # 방문한적 없다면
        if not visited[nxt]:
            # 방문 체그하고
            visited[nxt] = 1
            # 방문 예정지에 집어넣는 대신 함수를 실행(바로 방문)
            DFS(nxt)


DFS(1)


# endregion

# region swea 4875 미로

# 좌표값을 활용하여 dfs 구현
# 인접 행렬, 인접 리스트가 아니라 2차원 리스트 자체가 그래프를 나타냄
# 따라서 탐색은 델타 탐색을 활용

# 정점 -> 좌표 : 정점 번호가 없으니까
# 탐색 -> 델타 탐색 : 2차원 리스트니까

T = int(input())

# 델타 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# DFS
def DFS(r, c):
    global ans
    if maze[r][c] == 3:
        ans = 1
        return

    for d in range(4):
        # 새로운 좌표 찍어보기
        nr, nc = r + dr[d], c + dc[d]
        # 유효한지 검사(범위 조건) + 문제 조건(1이면 안됨, 아직 반문하지 않았을 것)
        # 단축 평가를 위해 범위 조건을 먼저 작성
        if (
            # 0 <= nr < N
            # and 0 <= nc < N and
            (nr, nc) not in visited
            and maze[nr][nc] != 1
        ):
            # 유효하다면?
            # 방문
            DFS(nr, nc)


for ts in range(1, T + 1):
    N = int(input())
    # maze =[list(map(int, input())) for _ in range(N)]
    # '10101' 리터러블 하기 때문에 하나의 문자씩 적용 됨

    # 패딩 기법
    maze = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        maze[i][1 : N + 1] = list(map(int, input()))
    ans = 0
    #################

    # 세팅(출발지, 예정지, 기록지)
    flag = False
    # for r in range(N):
    #     for c in range(N):
    # 패딩 기법을 사용하면 1씩 추가
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if maze[r][c] == 2:
                sr, sc = r, c
                flag = True
                break
        if flag:
            break

    visited = set([sr, sc])  # 출발지 좌표
    DFS(sr, sc)
    print(f"#{ts} {ans}")


"""
패딩 기법을 사용하여 벽인지 아닌지 확인하는 절차 생략 가능
방문한 곳을 1로 바꾸어 벽으로 바꾼다-> visited 확인 생략 가능

"""
# endregion


# region swea 5105 미로의 거리 bfs

from collections import deque

T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    #######################
    # 세팅(출발지, 예정지, 기록지)
    flag = False
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c
                flag = True
                break
        if flag:
            break
    queue = deque([(sr, sc, -1)])  # 문제 특성 상 0이 아닌 -1을 넣어줌
    visited = set([(sr, sr)])
    ans = 0
    # 예정지가 빌 때까지
    while queue:
        # 방문(큐에서 뽑기)
        r, c, cnt = queue.popleft()
        # 도착지 인지 검토
        if maze[r][c] == 3:
            ans = cnt
            break
        # 탐색 - 델타 탐색
        # 인접한 방향을 탐색해서
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if (
                0 <= nr < N
                and 0 <= nc < N
                and (nr, nc) not in visited
                and maze[nr][nc] != 1
            ):
                # 방문체크하고
                visited.add((nr, nc))
                # 방문예정지에 넣기
                queue.append((nr, nc, cnt + 1))
    print(f"#{tc} {cnt}")
# endregion


# region bono1012 유기농 배추
import sys

input = sys.stdin.readline

T = int(input())

# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(r, c):
    # 방문
    # 탐색 - 델타 탐색
    for d in range(4):
        # 네 방향을 보면서
        nr, nc = nr + dr[d], nc + dc[d]
        # 범위 유효성 + 1이라면?
        if 0 <= nr < N and 0 <= nc < N and field[r][c] == 1:
            # 방문체크하고
            visited.add((nr, nc))
            # 방문
            DFS(nr, nc)


for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())  # 문제에서 뒤집어 나옴
        field[r][c] = 1

    visited = set()
    ans = 0
    # 순회하며
    for r in range(N):
        for c in range(M):
            # 1이고, 방문한적 없다면?
            if field[r][c] == 1 and (nr, nc) not in visited:
                # 기록지에 추가
                visited.add((r, c))
                # DFS 또는 BFS
                DFS(r, c)
                # 정답 +1
                ans += 1

    print(ans)
# endregion

# region boj1012 유기농 배추
# 음수 좌표도 사용가능
# 좌표들의 집합이 중요하다
# 좌표만 있어도 이미 구조화 된 것임

# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = set()
    for _ in range(K):
        c, r = map(int, input().split())
        cabbages.add((r, c))

    cnt = 0

    while cabbages:
        # 아무거나 하나 꺼낸다, 집합에 있는건 양배추이다
        r, c = cabbages.pop()
        # 여기서 DFS
        # 예정지도 필요없음
        stack = [(r, c)]

        while stack:
            # 방문
            r, c = stack.pop()

            # 탐색 - 델타 탐색
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                # 유효성 검사 안해도됨
                # 2차원 리스트 없음, 무조건 양배추임
                if (nr, nc) in cabbages:
                    stack.append((nr, nc))
                    cabbages.discard((nr, nc))
        cnt += 1
    print(cnt)
# endregion

#region 노션 문제지에 양, 토마토 풀기 어려운거 풀 사람은 벽 부수고 이동하기


#endregion