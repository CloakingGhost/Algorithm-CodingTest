from heapq import heappop, heappush, heapify

# 임의의 리스트를 heap으로 만들어 줌
nums = [1, 2, 3, 6, 5, 4, 1, 2, 3, 1534, 7, 3, 77]
heapify(nums)
print(nums)

#
heap = []
heappush(heap, 5)
heappush(heap, 10)
heappush(heap, 1)
print(heap)

print(heappop(heap))
print(heappop(heap))
print(heappop(heap))

# 최대 힙
heappush(heap, -5)
heappush(heap, -10)
heappush(heap, -1)

print(-heappop(heap))
print(-heappop(heap))
print(-heappop(heap))