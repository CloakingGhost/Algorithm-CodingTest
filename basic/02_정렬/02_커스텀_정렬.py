# 내가 원하는 기준으로 정렬
# 1. 기본적인 방법을 이용한 커스텀 정렬
words = ["hello", "abd", "z"]
print(sorted(words))  # 기본적으로 알파벳 순서로 정렬


# 길이 순으로 정렬
def length(word):
    return len(word)


def reverse_length(word):
    return -len(word)


sorted_words = sorted(words, key=reverse_length)
print("길이 순으로 정렬:", sorted_words)

# 리스트 메서드
words = ["hello", "abd", "z"]
words.sort(key=length)  # 원본 리스트를 길이 순으로 정렬

# 2. 리스트를 원소로 갖는 리스트 커스텀 정렬
numbers = [[1, 13], [2, 7], [1, 7], [5, 10], [4, 20]]

print(sorted(numbers))  # 기본적으로 첫 번째 원소를 기준으로 정렬


### pair는 두 개의 원소를 갖는 리스트나 튜플을 의미
### unit은 리스트의 각 원소를 의미


# 두 번째 원소를 기준으로 정렬
# 오른차순 정렬
def custom_sort_key(unit):
    return unit[1]


sorted_numbers = sorted(numbers, key=custom_sort_key)
print("두 번째 원소를 기준으로 정렬:", sorted_numbers)


# 두 번째 원소를 기준,
# 만약 두 번재 원소가 같다면, 첫 번째 원소를 기준으로
# 오른차순 정렬
def custom_sort_key(unit):
    return unit[1], unit[0]  # 기준을 나열 할 수 있음(튜플)


sorted_numbers = sorted(numbers, key=custom_sort_key)
print("두 번째 원소를 기준으로 정렬:", sorted_numbers)


# 3. Lambda 활용하기
# "lambda 매개변수: 리턴값", 함수 간소화
def custom_sort_key(unit):
    return unit[1], unit[0]


# 추가 로직은 작성 불가, 리턴값만 있는 경우 사용
# sort_key = lambda unit: (unit[1], unit[0])
# sorted_numbers = sorted(numbers, key=sort_key)

sorted_numbers = sorted(numbers, key=lambda unit: (unit[1], unit[0]))
print("두 번째 원소를 기준으로 정렬:", sorted_numbers)


words = ["hello", "abd", "z"]


# 길이 순으로 정렬
def length(word):
    return len(word)


# 아래 두 과정이 동일하다고 이해 되면 지금 과정을 이해 한 것
sorted_words = sorted(words, key=lambda word: len(word))
sorted_words = sorted(words, key=len)
print(sorted_words)  # 기본적으로 알파벳 순서로 정렬


def absolute(number):
    return number if number >= 0 else -number
