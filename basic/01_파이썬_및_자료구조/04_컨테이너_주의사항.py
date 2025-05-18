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
