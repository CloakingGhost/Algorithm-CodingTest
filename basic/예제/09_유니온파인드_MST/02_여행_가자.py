# https://www.acmicpc.net/problem/1976

import sys


input = sys.stdin.readline

n, m = int(input()), int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
city = list(map(int, input().split()))


"""
3
3
0 1 0
1 0 1
0 1 0
1 2 3

5
5
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
5 3 2 3 4


"""
