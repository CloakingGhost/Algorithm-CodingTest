def solution(queries):
    queue = []
    answer = []
    for query in queries:
        if query == "pop":
            if queue:
                answer.append(queue.pop(0))  # O(N)
            else:
                answer.append(0)
        else:
            _, x = query.split()
            queue.append(int(x))
    return answer
