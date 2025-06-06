#region 조합 for문 
'''
20
7
23
19
10
15
25
8
13
'''
# for i in range(9)

# 아홉명 중에 일곱명을 뽑는다 == 아홉명 중에 두명을 뺀다
# 두개를 선택하여 전체 합에서 빼어 100이 되면
# 선택된 두명이 정답임

dwarfs = [int(input()) for _ in range(9)]
dwarfs_height = sum(dwarfs)
flag = False
for i in range(8):
  for j in range(1+i, 9) :
    if dwarfs_height - dwarfs[i] - dwarfs[j] == 100:
      spy=[i, j]
      flag = True
      break
  if flag :
    break

dwarfs = sorted(dwarfs)

for idx in range(9):
  if idx not in spy:
    print(dwarfs[idx])      

#endregion

#region 조합 투 포인터


dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
dwarfs_height = sum(dwarfs)
l =  0
r = len(dwarfs) - 1
target = 100

while(True):
  tmp = dwarfs_height - dwarfs[l] - dwarfs[r]
  if tmp < target:
    r -= 1
  elif tmp > target:
    l += 1
  else : # tmp == 100
    break

for idx in range(9):
  if idx != l and idx != r :
    print(dwarfs[idx])
#endregion