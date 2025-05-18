# 1. 순서가 있는 자료형 vs 순서가 없는 자료형
## list, string, tuple vs set, dict

# 2. 변경 가능한 자료형 vs 변경 불가능한 자료형
## list, dict, set vs string, tuple

# 3. 할당 vs 얕은 복사 vs 깊은 복사
# 3-1. 할당
a = [1, 2, 3]
b = a

print(a)
print(b)

## list는 mutable 함
b[0] = 4
print(a)
print(b)

## 3-2. 얕은 복사
from copy import copy

a = [1, 2, 3]
b = a[:]  # 복제 1
b = list(a)  # 복제 2
b = copy(a)  # 복제 3

b[0] = 4
print(a)
print(b)

## 3-3. 깊은 복사, 모든 값이 객체이기 때문
a = [[1, 2, 3], [4, 5, 6]]
b = a[:]

b[0][0] = 9
print(a)
print(b)

from copy import deepcopy

a = [[1, 2, 3], [4, 5, 6]]
b = deepcopy(a)

b[0][0] = 9
print(a)
print(b)
