# https://www.acmicpc.net/problem/1991
import sys

# 상수

LEFT, RIGHT, EMPTY = 0, 1, "."


def preorder(center):
    # 1. 종료조건
    if center == EMPTY:
        return
    # 2. 재귀식
    print(center, end="")
    preorder(tree[center][LEFT])
    preorder(tree[center][RIGHT])


def inorder(center):
    # 1. 종료조건
    if center == EMPTY:
        return
    # 2. 재귀식
    inorder(tree[center][LEFT])
    print(center, end="")
    inorder(tree[center][RIGHT])


def postorder(center):
    # 1. 종료조건
    if center == EMPTY:
        return
    # 2. 재귀식
    postorder(tree[center][LEFT])
    postorder(tree[center][RIGHT])
    print(center, end="")


input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")
