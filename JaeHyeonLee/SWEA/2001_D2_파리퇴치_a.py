def solved(flies, n, m):
    ans, tmp = 0, 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            for k in range(m):
                cur_row = k + i
                prev = j - 1
                next = j + m - 1
                # 다음행으로 오면 tmp 초기화
                if prev == -1:
                    tmp = 0
                    for r in range(m):
                        for c in range(m):
                            tmp += flies[r + i][c + j]
                    break
                # 직전 값 빼기
                tmp -= flies[cur_row][prev]
                # 다음 값 추가
                tmp += flies[cur_row][next]
            ans = max(ans, tmp)

    return ans


T = int(input())
for ts in range(1, T + 1):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{ts} {solved(flies, n, m)}")

"""

2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29




1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
"""
