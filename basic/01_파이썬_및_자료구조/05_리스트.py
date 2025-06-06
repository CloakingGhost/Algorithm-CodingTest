# 리스트
# 1. append O(1)
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
# 2. pop
numbers = [1, 2, 3]
number = numbers.pop()  # O(1)
print(number)

numbers = [1, 2, 3]
number = numbers.pop(0)  # O(n) 인덱스로 지정 가능
print(numbers)
print(number)

# 3. count O(n)
numbers = [1, 2, 3, 2]
counts = numbers.count(2)  # O(n)
print(counts)

# 4. sort O(nlogn): 병합정렬
numbers = [4, -1, 0, 2, 100]
numbers.sort()  # 원본이 변경 됨, mutable
print(numbers)
numbers.sort(reverse=True)  # 내림차순
print(numbers)
