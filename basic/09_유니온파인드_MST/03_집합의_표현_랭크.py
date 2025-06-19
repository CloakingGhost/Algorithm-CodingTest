# https://www.acmicpc.net/problem/1717
# 랭크(Union by Rank) == 트리의 높이
## 트리의 높이를 최소화
## 편향트리를 만들지 않기 위한 장치

"""
랭크가 작은 애가
큰 애 아래로
"""
import sys


# O(1)
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])  # Path Compression

    return parent[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    # 랭크를 이용해서 비교
    # 랭크가 다르면 랭크가 높은 집합에 랭크가 낮은 집합이 들어감
    # 랭크가 동일할 때는 아무데나 붙이고 랭크 + 1
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1


input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
rank = [0] * (n + 1)
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
