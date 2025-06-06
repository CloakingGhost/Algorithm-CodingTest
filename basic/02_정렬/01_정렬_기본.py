# 오름차순 정렬
# 내장함수 sorted(), 리스트 메서드 .sort() => O(n log n): 병합 정렬
numbers = [5, 2, 9, 1, 5, 6]
# set,tuple도 가능
sorted_numbers = sorted(numbers)  # 새로운 리스트를 반환
print("원본 리스트:", numbers)
print("오름차순 정렬:", sorted_numbers)

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # 원본 리스트를 정렬
print("원본 리스트:", numbers)


# 내림차순 정렬
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, reverse=True)  # 새로운 리스트를 반환
print("원본 리스트:", numbers)
print("내림차순 정렬:", sorted_numbers)

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)  # 원본 리스트를 정렬
print("원본 리스트:", numbers)
