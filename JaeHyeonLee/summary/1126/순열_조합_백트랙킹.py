from itertools import permutations

my_lst = ["A", "B", "C"]

print(list(permutations(my_lst)))
visited = [0, 0, 0]
# region
"""
각각의 데이터를 정점으로 하여
궤적을 그린다

"""


def DFS(depth):
    if depth == 3:
        return

    for nxt in range(3):
        if not visited[nxt]:
            visited[nxt] = 1
            DFS(depth + 1)
            visited[nxt] = 0 # 여기가 핵심


# endregion
