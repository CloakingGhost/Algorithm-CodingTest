#region
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()
ans = 0
l, r = 0, n - 1


while l < r :
  tmp = nums[l] + nums[r]
  if tmp == x :
    l += 1
    r -= 1
    ans += 1
    
  elif tmp > x:
    r -= 1
    
  elif tmp < x:
    l += 1
    
print(ans)
    



#endregion

#region
'''
x 가 되는 두 수의 합의 쌍을 구하는 문제


수열의 크기 n

수열의 수

목표 X
'''


#endregion