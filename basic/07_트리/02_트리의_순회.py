"""
트리순회
루트노드의 위치에 따라 명칭이 다름
전위: 루트 왼 오 - 먼저 찍고 내려(재귀)감
중위: 왼 루트 오
후위: 왼 오 루트

print가 루트에서 찍힘
"""

"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
# 상수
LEFT, RIGHT, EMPTY = 0, 1, None


# 전위 순회(Preorder)
def preorder(center):
    # 1. 종료조건
    ## 리프노드를 판단하지 않고
    ## 이동해서 center가 None인지 판단
    if center == EMPTY:
        return

    # 2. 재귀식
    print(center, end=" ")  # C
    preorder(tree[center][LEFT])  # L
    preorder(tree[center][RIGHT])  # R


# 중위 순회(Inorder)
def inorder(center):
    # 1. 종료조건
    ## 리프노드를 판단하지 않고
    ## 이동해서 center가 None인지 판단
    if center == EMPTY:
        return

    # 2. 재귀식
    inorder(tree[center][LEFT])  # L
    print(center, end=" ")  # C
    inorder(tree[center][RIGHT])  # R


# 후위 순회(Postorder)
def postorder(center):
    # 1. 종료조건
    ## 리프노드를 판단하지 않고
    ## 이동해서 center가 None인지 판단
    if center == EMPTY:
        return

    # 2. 재귀식
    postorder(tree[center][LEFT])  # L
    postorder(tree[center][RIGHT])  # R
    print(center, end=" ")  # C


n = int(input())
nodes = list(map(int, input().split()))
tree = [[EMPTY, EMPTY] for _ in range(n + 1)]

# 부모 : i
# 자식 : i + 1
# step : 2
for i in range(0, len(nodes), 2):
    parent = nodes[i]
    child = nodes[i + 1]

    if not tree[parent][LEFT]:
        tree[parent][LEFT] = child
    else:
        tree[parent][RIGHT] = child
# print(*tree, sep="\n")


preorder(1)
print()
inorder(1)
print()
postorder(1)
