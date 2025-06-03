# https://www.acmicpc.net/problem/20920

import sys
from collections import Counter

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
## 튜플에 담아서 하나씩 확인
words = [word for word in (input().rstrip() for _ in range(n)) if len(word) >= m]

# 풀이
## 빈도수
counter = Counter(words)
answer = sorted(counter.keys(), key=lambda unit: (-counter[unit], -len(unit), unit))

# 출력
print(*answer, sep="\n")
