# 문자열

# 1. join (무조건 문자열 원소들만 가능)
numbers = ["1", "2", "3", "4"]
joined_numbers = ",".join(numbers)  # ,로 연결
print(joined_numbers)  # 1,2,3,4

print("\n".join(numbers))

# 2. replace(old, new)
word = "hello python"
## imutable, 새로운 문자열을 만들어야 하기 때문
new_word = word.replace("python", "java")

# 3. 슬라이싱 string[start:end:step]
word = "hello"
print(word[1:3])  # el
print(word[0:4:2])  # hl
print(word[3:1:-1])  # ll
print(word[::-1])  # olleh
