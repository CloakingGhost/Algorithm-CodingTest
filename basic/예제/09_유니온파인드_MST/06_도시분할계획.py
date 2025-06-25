# https://www.acmicpc.net/problem/1647

import sys


def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return False

    if rank[x_root] > rank[y_root]:
        x_root, y_root = y_root, x_root

    parent[x_root] = y_root
    if rank[x_root] == rank[y_root]:
        rank[y_root] += 1

    return True


input = sys.stdin.readline

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

parent = list(range(n + 1))
rank = [0] * (n + 1)
edge_count = 0
max_cost = 0
total = 0

edges.sort(key=lambda x: x[-1])

for a, b, w in edges:
    if union(a, b):
        edge_count += 1
        total += w
        max_cost = w

        # 마지막 집을 하나의 마을로 취급
        # n이 2면 조건문 안들어감
        if edge_count == n - 2:
            # print(parent)
            # print(total)
            break
        # if edge_count == n - 1:
        #     break

# print(total - max_cost)
print(0 if n == 2 else total)
"""
6 7
1 2 100
2 3 100
3 4 100
4 5 100
5 6 100
1 6 50
2 5 10

4 6
1 2 1
1 3 1  
1 4 1
2 3 10
2 4 10
3 4 10

3 2
1 2 100
1 3 1

2 1
1 2 100

"""
