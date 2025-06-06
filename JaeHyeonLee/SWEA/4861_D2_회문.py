T = int(input())

def solved(words):
    # 0부터 n-m+1까지
    for i in range(n):
        for j in range(n - m + 1):
            flag = True
            for k in range(m//2):
                # i 행 고정 j 열에서 k 만큼 증가 
                # m-1에서 i 행 고정 j 열에서 k 만큼 감소
                if words[i][j + k] != words[i][m - 1 - k + j]:
                    flag = False
                    break
            if flag:
                return "".join(words[i][j : m + j])

            flag = True
            for k in range(m//2):
                # j 행에서 k 만큼 증가 i 열 고정정
                # m-1에서 j 행에서 k 만큼 감소 i 열 고정
                if words[j + k][i] != words[m - 1 - k + j][i]:
                    flag = False
                    break
            if flag:
                return "".join(words[j + idx][i] for idx in range(m))


for ts in range(1, T + 1):
    n, m = map(int, input().split())
    words = [list(input()) for _ in range(n)]
    # print(words)
    print(f'#{ts} {solved(words)}')
