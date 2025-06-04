# 파이썬에서는 큐도 리스트로 구현한다.
queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# dequeue
print(queue.pop(0))
print(queue.pop(0))

# peek
print(queue[0])
