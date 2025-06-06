import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


# x의 루트노드를 찾아 간다.
# find 연산을 개선하면 효율이 증가 함
# 개선을 위해 `경로 압축` 사용 됨
"""
기존 코드
루트노드를 찾고 종료 됨

개선 코드
재귀를 사용하여 루트노드를 찾으면
돌아오면서 경로의 있던 자식 노드들의
부모노드를 모두 루트노드로 바꾼다
마치 루트노드에 노드들이 달려있는 것처럼 정리하다
깊이가 1인 트리를 간이로 만든다

rank 리스트(트리의 높이)도 없어도 됨
깊이가 줄었기때문


"""





def find(x):
    if x != parent[x]:  # 루트노드가 아니면
        # 루트를 찾으러 가
        # 돌아올때(return) 부모노드를 루트노드로 바꾼다
        parent[x] = find(parent[x])
    return parent[x]


def find_old(x):
    while x != parent[x]:  # 루트노드가 아니면
        x = parent[x]  # x의 루트노드를 찾는다
    return x


def union(x, y):  # x가 속한 집단과 y가 속한 집합을 합친다
    if find(x) != find(y):
        # x의 루트노드에 y의 루트노드를 연결
        parent[find(x)] = find(y)  # 기존 코드


# 작은 트리를 큰 트리에 붙히면 깊이 증가 되지 않음
# 보조리스트 : 정점이 속한 트리의 깊이
def union_old(x, y):  # x가 속한 집단과 y가 속한 집합을 합친다
    if find(x) != find(y):
        # 개선 코드
        if rank[find(x)] > rank[find(y)]:
            parent[find(y)] = find(x)
        elif rank[find(x)] < rank[find(y)]:
            parent[find(x)] = find(y)
        else:  # rank[find(x)] == rank[find(y)]
            parent[find(x)] = find(y)
            # y노드가 속한 루트 노드가
            # x가 속한 루트 노드의 하위로 들어가기 때문에
            # y노드가 속한 루트노드의 rank를 하나 올림
            rank[find(y)] += 1



n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)  # find 연산 개선하면 생략가능
for _ in range(m):
    c, a, b = map(int, input().split())
    # make-set 연산 # 처음에는 자기 자신이다
    # 시간복잡도 영향을 준다
    # 트리의 깊이가 영향을 줌

    if c == 0:
        # union 연산(함수)
        union(a, b)

    elif c == 1:
        # find 연산(함수)
        # find(a) == find(b)?
        if find(a) == find(b):
            print("yes")
        else:
            print("no")
