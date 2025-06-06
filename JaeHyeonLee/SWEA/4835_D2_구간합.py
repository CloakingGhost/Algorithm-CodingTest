# region 문제 정리
"""
정렬을 하여 구간의 개수(M) 만큼 계산할 수도 있겠지만 
투 포인터 써보자

3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176


"""


# endregion

# region 풀이

T = int(input())

for ts in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    l, r = 0, M - 1
    tmp = sum(nums[:M])

    max_num, min_num = -float("INF"), float("INF")
    while True:
        max_num = max(max_num, tmp)
        min_num = min(min_num, tmp)
        tmp -= nums[l]
        l += 1
        r += 1
        if r >= N:
            break
        tmp += nums[r]
    print(f"#{ts + 1} {max_num - min_num}")

# endregion

# region 누적합(강사님 코드 참조)
# T = int(input())

# for ts in range(T):
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))

#     # 누적합 리스트
#     acc_lst = [0]
#     for num in nums:
#         acc_lst.append(acc_lst[-1] + num)

#     max_num, min_num = -float("INF"), float("INF")

#     for idx in range(N - M + 1):  # 전체 - 구간 + 1
#         tmp = acc_lst[idx + M] - acc_lst[idx]
#         max_num = max(max_num, tmp)
#         min_num = min(min_num, tmp)
#     print(f"#{ts + 1} {max_num - min_num}")


# endregion
