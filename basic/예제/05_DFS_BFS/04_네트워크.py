# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
from collections import deque


def solution(n, computers):

    def dfs(node):
        # 인덱스가 정점번호
        # 인덱스의 값으로 연결 여부 확인
        for next_node, value in enumerate(computers[node]):
            if value and not visited[next_node]:
                visited[next_node] = True
                dfs(next_node)

    def bfs(node):
        queue = deque([node])
        while queue:
            node = queue.popleft()

            for next_node, value in enumerate(computers[node]):
                if value and not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

    answer = 0
    visited = [False] * n
    for node in range(n):  # 정점
        if not visited[node]:
            visited[node] = True  # 방문 시작
            dfs(node)  # 연결 확인
            bfs(node)  # 연결 확인
            answer += 1  # 연결된 정점 확인 완료
    return answer


# [1, 1, 0],
# [1, 1, 0],
# [0, 0, 1]
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# [1, 1, 0],
# [1, 1, 1],
# [0, 1, 1]
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
