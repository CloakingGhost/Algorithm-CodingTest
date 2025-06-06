# region https://www.acmicpc.net/problem/10816
# endregion # 숫자 카드 2

import sys

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

counter = {}
for card in cards:
    counter[card] = counter.get(card, 0) + 1

for number in numbers:
    print(counter.get(number, 0), end=" ")

import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

counter = Counter(cards)
answer = [counter.get(n, 0) for n in numbers]
print(*answer)
