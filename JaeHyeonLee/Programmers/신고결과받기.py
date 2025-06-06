# region 문제 정리
"""
각 유저는 한번에 한 명만 신고
동일 유저 신고 1회로 처리 => set

k번 이상 신고된 유저 게시판 정지
해당 유저를 신고한 모든 유저에게 정지됐다는 사실을 알리는 메일 발송

한꺼번에 정지 시킨후 메일 발송

####################
입력값 

id_list: 모든 유저 정보

report : 신고자 피신고자

정지 기준 : k


결과

유저별 처리 결과 메일을 받은 횟수
즉, 신고자에게 알림 메일을 보내야 하는 횟수
피신고자가 정지 되었을때 마다
신고자의 메일카운트 증가

###############
이용자 신고자를 어떻게 식별?

set으로 중복 신고 제거
이용자 신고자 남아있음
신고자:[이용자,이용자]

신고자(key) 의 값의 길이 == k 면
전체 유저리스트에서 신고자의 값으로 있던 이용자들을 찾아 하나씩 올려준다

유저리스트-> 딕셔너리로 만든거 있으면 편하긴 할듯

준비물

1. 유저리스트 -> 유저딕셔너리
  1-1 신고자 딕셔너리 // { 신고자 : [이용자, 이용자], 신고자 : [이용자, 이용자] }
2. set으로 중복 제거
3. set 반복문 돌리면서 신고자에 따른 이용자 추가
4. 반복문 돌면서 신고자의 길이 >= k
  4-1 이용자에게 +1(유저딕셔너리 사용)

  
"""

# endregion

# region 풀이



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict, report_dict = {}, {}
    idx = 0
    for id in id_list:
        id_dict[id] = idx
        report_dict[id] = []
        idx += 1
        
    report_set = set(report)

    for r in report_set:
        reporter, reportee = r.split(" ")
        report_dict[reportee].append(reporter)

    for v_list in report_dict.values():
        print(v_list)
        if len(v_list) >= k:
            for v in v_list:
                answer[id_dict[v]] += 1
    return answer


print(solution(id_list, report, k))
# endregion