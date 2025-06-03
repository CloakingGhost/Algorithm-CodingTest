# https://school.programmers.co.kr/learn/courses/30/lessons/121683

# 2회 이상 나타난 알파벳이 2개 이상의 부분으로 나뉘어 있으면 안됨
# 연속으로 나타나야 함

# region
"""
1. 알파벳을 세는 딕셔너리 생성
2. 문자를 만나면
2 if. 문자가 딕셔너리에 있다면
  이미 한번 등장 했으므로 '외톨이 알파벳'으로 취급
  결과 리스트에 추가

2 else. 카운트 시작
   다른 문자가 나올때까지 카운트
   s, e를 둬야함
3. 다른 문자가 나오면
   s, e를 다른문자의 위치로 바꾼다
   "문자": "연속된 개수" <= e - s + 1

4. 문자열 끝까지 반복 후
5. 결과 리스트 정렬하여 ""로 join 하여 출력
"""
# endregion


def solution_old(input_string):

    counter = {}
    lonely_alphabet = set()
    s, e = 0, 0
    while s < len(input_string):
        char = input_string[s]
        # 등장한 적이 있다면
        if char in counter:
            # 외톨이 알파벳임
            lonely_alphabet.add(char)
        # 등장한 적이 없다면
        else:
            # 연속된 위치까지 e를 증가
            while e + 1 < len(input_string) and input_string[e + 1] == char:
                e += 1
            # {문자 : 연속된 개수} => 저장
            counter[char] = e - s + 1
        # 확인 안한 문자로 이동
        e += 1
        s = e
    # lonely_alphabet 정렬
    lonely_alphabet = sorted(list(lonely_alphabet))

    if len(lonely_alphabet) == 0:
        return "N"

    return "".join(lonely_alphabet)


def solution(input_string):

    counter = {}
    s, e = 0, 0
    while s < len(input_string):
        char = input_string[s]
        # 등장한 적이 있다면
        if char in counter:
            # 외톨이 알파벳임
            # 등장 횟수 증가
            counter[char] += 1
        # 등장한 적이 없다면
        else:
            # 연속된 위치까지 e를 증가
            while e + 1 < len(input_string) and input_string[e + 1] == char:
                e += 1
            # {문자 : 첫 무리 등장} => 저장
            counter[char] = 1
        # 확인 안한 문자로 이동
        e += 1
        s = e
    # counter 정렬
    answer = sorted([k for k, v in counter.items() if v != 1])

    if not answer:
        return "N"

    return "".join(answer)


print(solution("edeaaabbccd"))  # "de"
print(solution("eeddee"))  # "e"
print(solution("string"))  # "N"
print(solution("zbzbz"))  # "bz"
