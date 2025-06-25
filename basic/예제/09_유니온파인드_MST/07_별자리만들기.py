# https://www.acmicpc.net/problem/4386

import sys

sys.setrecursionlimit(10**6)


def get_distance(star_1, star_2):
    x1, y1 = star_1
    x2, y2 = star_2
    x = (x2 - x1) ** 2
    y = (y1 - y2) ** 2
    return (x + y) ** 0.5 // 0.01 / 100


idx = 0


def put_star(star):
    global idx
    if dict.get(star) is None:
        dict[star] = idx
        idx += 1


def combinations(start, current):
    # 종료 조건
    if len(current) == 2:
        star_1, star_2 = current[0], current[1]
        distance = get_distance(star_1, star_2)

        # 인덱스 화
        put_star(star_1)
        put_star(star_2)

        # 거리값 추가
        edges.append(current[:])
        edges[-1].append(distance)
        return
    # 재귀식
    for i in range(start, len(stars)):
        current.append(stars[i])
        combinations(i + 1, current)
        current.pop()


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
n = int(input())
# 좌표를 인덱스로 바꿔야함
dict = {}
stars = [tuple(map(float, input().split())) for _ in range(n)]
edges = []
print(f"stars : {stars}")
combinations(0, [])

print(edges)


edges.sort(key=lambda x: x[-1])
parent = list(range(n))
rank = [0] * (n)
edge_count = 0
total = 0
for a, b, distance in edges:
    a = dict.get(a)
    b = dict.get(b)
    if union(a, b):
        edge_count += 1
        total += distance
        if edge_count == n - 1:
            break

print(total)


"""
3
2.0 4.0
2.0 2.0
1.0 1.0

3
2.01 4.01
2.01 2.01
1.01 1.01

3
1.0 1.0
-1.0 1.0
-1.0 -1.0
"""

# print(list(map(float, "-1.0 -1.0".split())))
