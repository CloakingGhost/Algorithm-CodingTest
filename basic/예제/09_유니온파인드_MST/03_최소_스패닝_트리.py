# https://www.acmicpc.net/problem/1197

import sys


def find(x):
    root = x
    while root != parent[root]:
        root = parent[root]

    while x != root:
        parent[x] = root
        x = parent[x]
    return root


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return False

    if rank[x_root] < rank[y_root]:
        x_root, y_root = y_root, x_root

    parent[y_root] = x_root
    if rank[x_root] == rank[y_root]:
        rank[x_root] += 1

    return True


input = sys.stdin.readline

v, e = map(int, input().split())
parent = list(range(v + 1))
rank = [0] * (v + 1)
edges = [tuple(map(int, input().split())) for _ in range(e)]

edges.sort(key=lambda x: x[-1])

edge_count = 0
weight = 0
for a, b, w in edges:
    if union(a, b):
        edge_count += 1
        weight += w

        if edge_count == v - 1:
            break
print(weight)


"""
3 3
1 2 1
2 3 2
1 3 3

3 3
1 2 1
2 3 2
1 3 -3
"""
