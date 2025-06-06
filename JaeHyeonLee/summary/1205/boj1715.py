from heapq import heapify, heappop, heappush

N = int(input())

heap = []
for _ in range(N):
    card = int(input())
    heappush(heap, card)
    # 카드뭉치가 1개 남을 때까지 반복

ans = 0

while len(heap) > 1:
    c1, c2 = heappop(heap), heappop(heap)
    # 가장 작은 두 값을 합치고
    c = c1 + c2
    # 더한 값(비교횟수)를 누적
    ans += c
    # 더한 값 힙에 추가
    heappush(heap, c)
print(ans)