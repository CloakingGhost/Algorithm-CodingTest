# https://www.acmicpc.net/problem/1068
import sys

EMPTY = -1
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n)]
parents = list(map(int, input().split()))
delete_node = int(input())
root = None
for node in range(n):
    parent = parents[node]

    if parent == EMPTY:
        root = node
        continue

    if delete_node == node:
        continue

    tree[parent].append(node)


# 탐색


def dfs(parent):
    if not tree[parent]:
        return 1

    count = 0

    for next_node in tree[parent]:
        count += dfs(next_node)
    return count


if delete_node == root:
    print(0)
else:
    print(dfs(root))


"""
6
-1 0 0 0 1 1
2

5
0 0 1 1 -1
2
"""
