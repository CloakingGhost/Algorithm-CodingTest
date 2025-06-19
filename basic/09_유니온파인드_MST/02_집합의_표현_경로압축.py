# https://www.acmicpc.net/problem/1717
# 경로압축(Path Compression)
import sys

sys.setrecursionlimit(10**6)


# O(1)
def find_old(x):
    # 1. 종료 조건
    if x == parent[x]:
        return parent[x]

    # 2. 재귀식
    ## 대표원소를 찾아서 경로의 모든 원소의 부모노드를 대표원소로 변경
    parent[x] = find_old(parent[x])  # Path Compression

    # 대표원소 반환
    return parent[x]


# O(1)
def find(x):
    # 1. 종료 조건
    if x != parent[x]:
        # 2. 재귀식
        ## 대표원소를 찾아서 경로의 모든 원소의 부모노드를 대표원소로 변경
        parent[x] = find(parent[x])  # Path Compression

    # 대표원소 반환
    return parent[x]


def union(x, y):
    # 대표원소 찾기
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
answer = []
for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            answer.append("YES")
        else:
            answer.append("NO")

print("\n".join(answer))
