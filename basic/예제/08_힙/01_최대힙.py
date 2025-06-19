# https://www.acmicpc.net/problem/11279
from heapq import heappush, heappop
import sys


input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(heap, -x)
    else:
        if heap:
            print(-heappop(heap))
        else:
            print(0)
