# region 개념
"""
그래프 : 점과 선으로 이루어져 있음

파이썬 문법으로 구조화

점(v:vertex) : 정점, 버텍스
간선(e:edge) : 정점의 연결
가중치 : 간선에 부여되는 값, 비용// 최단거리에 사용

유방향: 간선에 방향이 있음

입력값 A B 로 주어진다면
A -> B 의 일방향임

무방향: 방향이 없어 양방향으로 이동가능 하다

이러한 정보는 구조화 할 때 사용 됨

희소(간선이 적음) , 밀집(간선이 빽빽), 완전(가능한 모든 정점 사이에 간선이 연결되어 있는 그래프)
간선의 개수
E = V - 1


구조화 2가지

1. 인접행렬 (adj matrix)
- 정점 간 연결 관계를 2차원 배열로 표현하는 방식
행번호 출발지
열번호 도착지

2. 인접리스트


"""


# endregion

# region 실습 인접 행렬

"""
7
7
0 1
1 2
0 4
4 1
4 5
3 6
6 5


7
7
0 1 3
1 2 4
0 4 2
4 1 9
4 5 7
3 6 2
6 5 6
"""

"""
V = int(input()) # 정점
E = int(input()) # 간선

# 1. 빈 판 만들기(V * V)
adj_matrix = [[0]*V for _ in range(V)]
# print(adj_matrix)

# 2. 간선 정보 입력받기
for _ in range(E) :
  # s, e = map(int, input().split())
  s, e, w = map(int, input().split())
  # adj_matrix[s][e] = 1 # 일방향
  # adj_matrix[e][s] = 1 # 양방향
  adj_matrix[s][e] = w # 일방향, 가중치
  adj_matrix[e][s] = w # 양방향, 가중치

print(adj_matrix)
"""
# endregion

# region 실습 인접 리스트, 일반적으로 더 효율적임
# 도착지만 담기 때문에 조회수가 적음

# 행번호 출발지
# 도작치의 정점 번호가 리스트에 담김
"""
V = int(input())  # 정점
E = int(input())  # 간선
# 1. 빈 판 만들기(빈 리스트 V개가 들어잇는 이차원 리스트)
adj_lst = [[] for _ in range(V)]

print(adj_lst)
# 2. 간전정보 입력 받기
for _ in range(E):
    s, e, w = map(int, input().split())
    # s, e = map(int, input().split())
    # adj_lst[s].append(e) # 단방향
    # adj_lst[e].append(s) # 양방향
    adj_lst[s].append((w, e))  # 단방향
    adj_lst[e].append((w, s))  # 양방향
    """
# endregion

# region boj2606
# 0번 인덱스는 만들고 안쓰면 그만
"""
V = int(input())
E = int(input())

# 빈 판 만들기
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    s, e = map(int, input().split())
    adj_matrix[s][e] = 1
    adj_matrix[e][s] = 1
print(adj_matrix)


V = int(input())
E = int(input())

# 빈 판 만들기
adj_lst = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e = map(int, input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)
print(adj_lst)
"""

# endregion

# region 각 구조화의 특징
""" 

행렬 : 방향 전환이 빠르다, 전치 문제에 효과적

리스트 : 탐색이 빠름, 간선이 빽빽하지 않다면 빠르다, 일반적으로 많이 사용 됨


"""

# endregion
########################################################

# region 그래프 완전 탐색
"""
1. 그래프의 모든 정점을 방문
2. 중복없이 방문

기록지 : 방문한 곳 기록, 다시 방문하지 않도록
어디로 먼저가지 묶어둘 곳

방문 예정지 : 갈 수 있는 곳, 탐색된 곳을 넣어 놓는다, 인접 리스트 || 인접 행렬

더이상 갈 수 없다 == 방문 예정지가 비었다

예정지에 값이 중복 될 수 있다
그러나 기록지와 방문여부를 비교하기 때문에 
예정지에 중복이 되어도 방문은 1회만 실시한다.


임의의 정점을 방문


DFS(깊이우선탐색) : 재귀로 구현하면 코드가 깔끔해짐
가장 최근에 탐색된 정점을 우선적으로 방문하는 탐색 방법
예정지로 "스택"(또는 시스템스택)을 사용
방문 궤적이 "경로"를 이루며 탐색


궤적(기록지) path = []
예정지 stack = []


BFS(너비우선탐색) : 최단거리 알고리즘
가장 먼저 탐색된 정점을 우선적으로 방문하는 탐색 방법
예정지로 "큐"를 사용
시작 정점으로부터 가까운 정점

궤적(기록지) path = []
예정지 queue = []

동심원을 그리며 방문
방문중 동일 레벨외에는 넘어갈 수 없다.


공통사항 
탐색이 되었다 -> 방문을 언젠가 한다.
즉, 방문할 거니까 방문했다고 미리 체크
"""


# endregion

# region DFS BFS
# 초기 세팅(출발지, 기록지, 예정지)

# 예정지가 빌 때까지
# 예정지에서 꺼내서 방문

# 방문한 곳에서 갈 수 있는 곳 탐색(인접리스트)
# 방문한 적이 없는 곳이라면?(기록지에서 확인)
# 방문체크하고
# 예정지에 집어 넣는다


# 기록지는 엄청나게 많이 확인 한다
# 집합으로 만들자

# endregion

# region 코드 템플릿 BFS, visited = set
from collections import deque

"""
# 초기 세팅(출발지, 기록지, 예정지)
queue = deque([1])  # 예정지([출발지])
visited = set([1])  # 기록지

# 예정지가 빌 때까지
while queue:
    # 예정지에서 꺼내서 방문
    cur = queue.popleft()
    # 방문한 곳에서 갈 수 있는 곳 탐색(인접리스트)
    for nxt in adj_lst[cur]:  # 인접리스트의 cur 번째에 있음
        # 방문한 적이 없는 곳이라면?(기록지에서 확인)
        if nxt not in visited:
            # 방문체크하고
            visited.add(nxt)
            # 예정지에 집어 넣는다
            queue.append(nxt)
"""

# endregion
# region 코드 템플릿 BFS, visited = list
from collections import deque

# 초기 세팅(출발지, 기록지, 예정지)
"""
queue = deque([1])  # 예정지([출발지])
visited = [0] * (V+1)  # 기록지

# 예정지가 빌 때까지
while queue:
    # 예정지에서 꺼내서 방문
    cur = queue.popleft()
    # 방문한 곳에서 갈 수 있는 곳 탐색(인접리스트)
    for nxt in adj_lst[cur]:  # 인접리스트의 cur 번째에 있음
        # 방문한 적이 없는 곳이라면?(기록지에서 확인)
        if nxt not in visited:
            # 방문체크하고
            visited.add(nxt)
            # 예정지에 집어 넣는다
            queue.append(nxt)

"""
# endregion
# region 코드 템플릿 DFS
# 출발지, 예정지, 기록지
"""
stack = deque([1])
visited = set([1])


# 예정지가 빌 때까지
while stack:
    # 예정지에서 하나 꺼내
    cur = stack.pop()
    # 다음거 있는지 찾아(인접리스트에)
    for nxt in stack[cur]:
        # 리스트에 있는거 하나씩 꺼내
        if nxt not in visited:
            # 꺼낸거 기록지에 있는지 확인, 기록지에 없으면
            # 기록지에도 추가
            visited.add(nxt)
            # 예정지에 추가
            stack.append(nxt)

"""
# endregion

# region boj2606


V = int(input())
E = int(input())

adj_lst = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e = map(int, input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)

# print(adj_lst)

queue = deque([1])
# visited = set(adj_lst[1])
visited = [0] * (V + 1)
visited[1] = 1

while queue:
    cur = queue.popleft()
    for nxt in adj_lst[cur]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)

print(sum(visited))

# endregion

# region boj11724

import sys
input = sys.stdin.readline
def DFS(start):
    # 초기 세팅 (출발지, 기록지, 예정지)
    stack = [start]

    # 예정지가 빌 때까지
    while stack:
        # 방문
        cur = stack.pop()

        # 탐색(인접행렬)
        for nxt in range(1, V + 1):
            # 방문하지 않은 곳이라면?
            if adj_matrix[cur][nxt] and nxt not in visited:
                # 방문체크하고
                visited.add(nxt)
                # 예정지에 집어넣는다
                stack.append(nxt)


V, E = map(int, input().split())

# 1. 빈 판
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 2. 간선 정보 입력받기
for _ in range(E):
    s, e = map(int, input().split())
    adj_matrix[s][e] = 1
    adj_matrix[e][s] = 1

######################################
visited = set()
cnt = 0

# 정점을 하나씩 돌면서
for node in range(1, V + 1):
    # 방문한적 없는 정점이라면?
    if node not in visited:
        # 방문체크하고
        visited.add(node)
        # DFS
        DFS(node)
        # 1 카운팅
        cnt += 1

print(cnt)
# endregion


#region DFS vs BFS

'''
완전탐색 - 무방
경로의 특징 - DFS
최단거리 + 가중치 X - BFS
최단거리 + 가중치 X - 다익스트라

'''



#endregion