# region 문제 정리
"""
특정 범위의 물건 싹슬이

모든 종류의 보석을 적어도 1개 이상을 가진 구간
모든 종류??



###############
입력 

gems: 리스트

출력
모든 종류의 보석이 있는
진열대 시작 번호, 진열대 끝 번호

################
입력된 리스트 -> set : 중복제거
set -> 딕셔너리 { 상품 : 0 }

반복문 돌면서
상품마다 1씩 더하는데
l 인덱스의 상품  == r 인덱스의 상품
l += 1
그리고 l위치의 상품이 딕셔너리의 값이 2 이상이면 하나 빼고 l 이동
또 그위치의 값이 2 이상이면 하나 빼고 l 이동 
r보다 작으면서 1까지 반복


r_gem의 값이 1 이상이면 다른 잼들 중 0이 없으면 종료
idx가 set 크기만큼 돌았으면 종료
set.values() 



r < len(gems) 까지 무한반복


"""

# endregion

# region 풀이
# gems = ["AB", "AA", "AA", "AA", "AA", "AA", "AA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]


def solution(gems):
    l, r = 0, 0
    gems_dict = {v: 0 for v in set(gems)}
    kind = len(gems_dict)
    cur_kind = 0
    while r < len(gems):
        r_gem = gems[r]
        if gems_dict[r_gem] == 0:
            cur_kind += 1
        elif kind == cur_kind:
            break
        gems_dict[r_gem] += 1
        r += 1

        if gems[l] == r_gem:

            while l < r:
                l_gem = gems[l]
                if gems_dict[l_gem] > 1:
                    gems_dict[l_gem] -= 1
                    l += 1
                else:
                    break

    answer = [l + 1, r]
    return answer


print(solution(gems))
# endregion
