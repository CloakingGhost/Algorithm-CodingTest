# https://www.acmicpc.net/problem/16165

import sys


# quiz_type = "0":팀이름 => 모든 멤버의 이름 사전순 한 줄 씩
# quiz_type = "1":멤버이름 => 멤버가 속한 팀 이름
def solve_quiz(quiz, quiz_type):
    if quiz_type == "0":
        return singers[quiz]
    else:
        for group, members in singers.items():
            if quiz in members:
                return [group]


input = sys.stdin.readline
n, m = map(int, input().split())
singers = {}
for _ in range(n):
    group = input().rstrip()
    num = int(input())
    singers[group] = []
    for i in range(num):
        singers[group].append(input().rstrip())
        if i == num - 1:
            singers[group].sort()


for _ in range(m):
    quiz = input().rstrip()
    quiz_type = input().rstrip()

    print("\n".join(solve_quiz(quiz, quiz_type)))
