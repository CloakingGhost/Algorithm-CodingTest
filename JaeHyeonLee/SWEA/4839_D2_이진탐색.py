# region 문제 정리
"""

책이 총 400쪽이면,
검색 구간의 왼쪽 l=1,
오른쪽 r=400이 되고,
중간 페이지 c= int((l+r)/2)로 계산

찾는 쪽 번호(target)가 c와 같아지면 탐색을 끝낸다.

이긴 사람이 누구인지 알아내 출력하시오.
비긴 경우는 0을 출력

"""


# endregion

# region 풀이


def binary_search(l, r, target):
    count = 0
    while l <= r:
        c = (l + r) // 2
        count += 1
        if c == target:
            return count
        elif c > target:
            r = c
        elif c < target:
            l = c
        print(l, r)
    return count

T = int(input())
for ts in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    a, b = binary_search(1, P, Pa), binary_search(1, P, Pb)
    print(a, b)
    ans = 0
    if a < b:
        ans = "A"
    elif a > b:
        ans = "B"
    print(f"#{ts} {ans}")

# endregion
