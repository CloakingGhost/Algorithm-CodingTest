# https://www.acmicpc.net/problem/1068
import sys

LEFT, RIGHT, EMPTY = 0, 1, -1
input = sys.stdin.readline
n = int(input())
tree = [[EMPTY, EMPTY] for _ in range(n)]
nodes = list(map(int, input().split()))
for node in range(1, n):
    parent = nodes[node]
    if node % 2:
        tree[parent][LEFT] = node
    else:
        tree[parent][RIGHT] = node

delete_node = int(input())

parent = delete_node // 2
if tree[parent][LEFT] == delete_node:
    tree[parent][LEFT] = EMPTY
else:
    tree[parent][RIGHT] = EMPTY

# 탐색
count = 0


def preorder(center):
    global count
    if tree[center][LEFT] == EMPTY and tree[center][RIGHT] == EMPTY:
        count += 1
        return

    if tree[center][LEFT] != EMPTY:
        preorder(tree[center][LEFT])

    if tree[center][RIGHT] != EMPTY:
        preorder(tree[center][RIGHT])


if delete_node == 0:
    print(0)
else:
    preorder(0)

    print(count)
