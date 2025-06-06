# region 문제 정리
'''
1. 무식하게 풀기
아무 정점 잡아서 모두 탐색


어떻게 구조화를 해야하며
어떻게 간선을 끝을 것인지 구현해야 함

'''

# endregion

# region 풀이

def solution(n, wires):
    def DFS(start):
        # 초기 세팅(출발지, 예정지, 기록지)
        stack = [start]
        visited = set([start])
        # cnt = 1 # visited에 쌓임
        
        # 예정지가 빌 때까지
        while stack :
            # 방문
            cur = stack.pop()
            # 탐색
            # 갈 수 있는 곳을 찍어서
            for nxt in range(1, n+1):
                # 갈 수 있다면(방문한적 없다면?)
                if adj_matrix[cur][nxt] and nxt not in visited:
                    # 방문체크하고
                    visited.add(nxt)
                    # 예정지에 넣기
                    stack.append(nxt)
                    # cnt += 1 # visited에 쌓임
        return abs(2*len(visited) - n) # a + b = n 
    # 구조화
    adj_matrix = [[0] * (n+1) for _ in range(n+1)]
    for a, b in wires:
        adj_matrix[a][b] = 1
        adj_matrix[b][a] = 1
  
    answer = float("INF")
    
    # 모든 간선에 대해서
    for a, b in wires:
        # 간선 하나를 잘라보고
        adj_matrix[a][b] = adj_matrix[b][a] = 0
        # DFS/BFS 돌린 후에 정답을 갱신
        # 아무 정점 1개를 잡고 시작하면 됨, 완전 탐색을 해야하기 때문
        answer = min(answer, DFS(1))
        # 간선 다시 붙이기
        adj_matrix[a][b] = adj_matrix[b][a] = 1
    return answer


# endregion