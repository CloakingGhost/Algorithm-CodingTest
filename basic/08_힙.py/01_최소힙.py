# 최소힙
from heapq import heappush, heappop

heap = []

# 삽입
heappush(heap, 5)
heappush(heap, 2)
heappush(heap, 7)
heappush(heap, 3)
heappush(heap, 0)
heappush(heap, -1)

print(heap)

# 삭제
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))

# 문자열도 됩니다.
heap = []

heappush(heap, "a")
heappush(heap, "x")
heappush(heap, "f")

print(heap)

print(heappop(heap))
print(heappop(heap))
print(heappop(heap))

# 리스트나 튜플도 됩니다.
heap = []

heappush(heap, [1, 2])
heappush(heap, [2, 3])
heappush(heap, [1, 3])

print(heap)

print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
