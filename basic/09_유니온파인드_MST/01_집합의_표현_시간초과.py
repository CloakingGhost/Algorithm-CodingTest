# https://www.acmicpc.net/problem/1717
import sys


# O(n)
def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


# union 50000번 할 때
# find 한번당 50000번을 해야함
# 그런데 find를 50000번 하면
# 50000 x 50000번을 해야함
# 결론, 오래걸림
def union(x, y):
    # 대표원소 찾기
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
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
