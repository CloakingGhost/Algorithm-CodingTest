import sys

input = sys.stdin.readline
users = {}
N, M = map(int, input().split())
for _ in range(N + M):
    name = input().rstrip()
    if name in users:
        users[name] += 1
    else:
        users[name] = 1

answer = []
for key, value in users.items():
    if value == 2:
        answer.append(key)

answer.sort()
print(len(answer))
print(*answer, sep="\n")
# print("\n".join(answer))

import sys
from collections import Counter

# 입력
input = sys.stdin.readline
N, M = map(int, input().rsplit())
names = [input().rstrip() for _ in range(N + M)]

# 풀이
users = Counter(names)
answer = sorted([name for name, count in users.items() if count == 2])

# 출력
print(len(answer))
print(*answer, sep="\n")
