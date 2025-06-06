# 1647 도시 분할 계획
"""
최소신장트리 만들고

가중치가 가장 큰 간선 1개를 끊는다
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find(x):
    if x != parent[x]:  # 루트노드가 아니면
        # 루트를 찾으러 가
        # 돌아올때(return) 부모노드를 루트노드로 바꾼다
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):  # x가 속한 집단과 y가 속한 집합을 합친다
    if find(x) != find(y):
        # x의 루트노드에 y의 루트노드를 연결
        parent[find(x)] = find(y)  # 기존 코드


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])  # 가중치 기준으로 오름차수 정렬
parent = [i for i in range(N + 1)]
cnt = ans = 0

# 간선을 하나씩 꺼내서
for a, b, w in edges:
    # 연결할 수 없다면(사이클이 생긴다면)
    if find(a) == find(b):
        # 그냥 넘어간다
        continue

    # 연결할 수 있다면(사이클이 생기지 않는다면)
    # 연결하고
    union(a, b)
    # 간선 하나 세어주기(cnt)
    cnt += 1
    # 가중치를 더해준다(ans)
    ans += w

    # 간선을 몇 개 뽑았는지 검토
    if cnt == N - 1:
        # N - 1개 뽑았다면? => 마지막 가중치를 빼주고 종료
        ans -= w
        break

print(ans)