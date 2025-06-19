"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

n = int(input())
nodes = list(map(int, input().split()))
tree = [[None, None] for _ in range(n + 1)]

# 부모 : i
# 자식 : i + 1
# step : 2
for i in range(0, len(nodes), 2):
    parent = nodes[i]
    child = nodes[i + 1]

    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
print(*tree, sep="\n")
