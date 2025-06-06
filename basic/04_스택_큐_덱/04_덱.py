from collections import deque

# double ended queue
queue = deque()

# enqueue (앞, 뒤)
queue.appendleft(1)
queue.appendleft(2)
queue.append(3)
queue.append(4)

# dequeue (앞, 뒤)
print(queue.popleft())
print(queue.pop())

# peek (앞, 뒤)
print(queue[0])
print(queue[-1])

# 덱이 앞뒤 관련 시간복잡도가 유리하다
# 그러나 중앙에 있는 값을 찾을 때는 분리
# 앞 혹은 뒤에서 부터 들어가기 때문
# O(n/2) => O(n) : 상수 제외
