# region 투 포인터
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]
    ans = 0
    for i in range(k):
        for j in range(k):
            if i != j:
                word = words[i] + words[j]

                # 회문 확인
                l = 0
                r = len(word) - 1
                flag = True
                while l < r:
                    if word[l] == word[r]:
                        l += 1
                        r -= 1
                    else:
                        flag = False
                        break
                if flag:
                    ans = word
        if flag:
            break
    print(ans)        
# endregion
