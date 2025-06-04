def solution(queries):
    stack = []
    answer = []

    for query in queries:
        if query == "pop":
            if stack:
                answer.append(stack.pop())
            else:
                answer.append(0)
        else:
            _, x = query.split()
            stack.append(int(x))
    return answer
