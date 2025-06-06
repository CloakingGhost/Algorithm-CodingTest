# region 
from itertools import permutations

cities = ['A', 'B', 'C']

# print(list(permutations(cities)))


'''
    [ 0   0   0 ]
      A   B   C
0     A 
1
2

탐색 즉시 방문 표시하고 다음 depth로 이동
A 방문 했으니 
B 방문한다

B 방문 후
다시 A 부터 확인
A 방문했음
B 방문했음
C는 아직 안했음
더이상 갈 곳이 없으니 
C 뽑고 인쇄실에 저장

리턴하면서
C 방문 체크 해제시켜 준다.
올라가면서
B 방문 체크 해제
근데 B에서 C를 방문한적이 없다
2depth 에서 C를 해제 했으므로
1depth에서 C를 방문하게 된다.

이제 2depth에서 B를 방문하고
인쇄실에서 기록 저장

이제 리턴하면서 B 방문해제
C까지 확인해 보니 방문을 했음
올라가서 1depth c 체크 해제

0depth 체크 해제
이제 0depth B 방문
1depth 에서 A 부터 확인



'''

# endregion