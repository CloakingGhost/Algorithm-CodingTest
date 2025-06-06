# region 문제정리

"""
N : 전제 날짜 수
K : 1 <= K <= N 연속적인 날짜 수


1. 누적합 배열 만들기
 
2. N - K + 1까지 반복하며 
  현재값과 임시값 중 큰값 찾기
"""
# endregion

# region 풀이
N, K = map(int, input().split())
nums = list(map(int, input().split()))

acc_lst = [0]
for num in nums:
    acc_lst.append(acc_lst[-1] + num)
max_num = -float("INF")
for i in range(N - K + 1):
  tmp = acc_lst[i + K] - acc_lst[i]
  max_num = max(max_num, tmp)
  
print(max_num)
# endregion


# region 깨달은 점
'''
누적합 배열을 사용하면 초기값이 0인덱스에 추가되기 때문에 -1을 할 필요 없음

print를 활용하여 누적합 배열을 끝까지 사용하는지 확인


'''


# endregion