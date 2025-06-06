"""
유니온파인드는 싸이클 판별에 유용함
이미 연결되어서 하나의 집합으로 구조화된 되어 있는 정점은
집합에서 연결이 되면 싸이클이 발생한다



싸이클이 발생하는 지점을 출력하는 문제
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


n, m = map(int, input().split())

parent = list(range(n))  # 정점의 루트 노드 구조화

for cnt in range(1, m + 1):
    a, b = map(int, input().split())

    # 서로 다른 정점의 루트노드가 같다면
    # 싸이클 발생
    if find(a) == find(b):
        print(cnt)
        break
    
    union(a, b)
else: 
  print(0)