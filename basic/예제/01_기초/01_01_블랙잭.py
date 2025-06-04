# https://www.acmicpc.net/problem/2798
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
answer = sum(numbers[:3])

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            tmp = numbers[i] + numbers[j] + numbers[k]
            if tmp <= m:
                answer = max(answer, tmp)
            else:
                break

print(answer)
