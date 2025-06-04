from collections import deque


def solution(queries):
    queue = deque()
    answer = []

    for query in queries:
        if query == "removeFirst":
            if queue:
                answer.append(queue.popleft())
            else:
                answer.append(0)
            continue
        if query == "removeLast":
            if queue:
                answer.append(queue.pop())
            else:
                answer.append(0)
            continue

        command, x = query.split()

        if command == "addFirst":
            queue.appendleft(int(x))
        else:
            queue.append(int(x))

    return answer
