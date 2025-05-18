# List comprehension
numbers = [i for i in range(1, 6)]
print(numbers)
numbers = [i for i in range(1, 6) if i % 2 == 0]
print(numbers)

# packing, unpacking
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)
print(*numbers)

# enumerate
for i in range(len(numbers)):
    print(f"{i} 번째 원소 : {numbers[i]}")

for i, number in enumerate(numbers):
    print(f"{i} 번째 원소 : {number}")

# Counter
numbers = [1, 2, 4, 1, 2, 2, 3, 2, 2]
counter = {}
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(counter)

from collections import Counter

counter = Counter(numbers)
print(counter)
common = counter.most_common()
print(common[0])
