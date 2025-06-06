# region 문제 정리
'''
N개 주어짐

단어를 정렬하여 하나씩 출력

짧은것 부터
같은길이 사전순
a < b -> a 출력

중복 제거 해야함
'''

# endregion

# region 풀이
import sys
input=sys.stdin.readline
N = int(input())
words = [input().rstrip() for _ in range(N)]
words = list(set(words))#  중복 제거 후 리스트로
words.sort(key=lambda x : (len(x), x))
for w in words:
  print(w)
# endregion