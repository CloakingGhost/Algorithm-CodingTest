# region 문제 정리
"""
https://www.acmicpc.net/problem/1449

길이 L 테이프 : 무한개
파이프 물이 새는 곳 좌우 0.5는 막아야함

테이프는 겹쳐서 붙일 수 있음음


input
물이 새는 곳 위치
테이프 길이

output
필요한 테이프 개수

4 2
1 2 100 101


4 3
1 2 3 4

3 1
3 2 1
"""
# endregion

# region 풀이
import sys

input = sys.stdin.readline


def solved(holes):
    # 구멍의 위치는 자연수 이므로 1개는 기본값
    # 구멍 반드시 존재
    ans = 1
    # 시작 지점(구멍)
    start = holes[0]
    # 구멍 하나씩 꺼냄
    for idx in range(n):
        hole = holes[idx]
        # 시작 구멍으로 부터 테이프 길이까지
        # 없으면 테이프 범위 벗어나므로
        # start 다음 위치로 이동
        if hole not in range(start, start + l):
            start = holes[idx]
            # 필요한 테이프 개수 추가
            ans += 1
    return ans


n, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
print(solved(holes))




# endregion