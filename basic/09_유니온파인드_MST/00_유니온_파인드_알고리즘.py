"""
set 이 있음에도 배우는 이유

# 유니온
집합 A(N개)
집합 B(M개) 가 있을때
합집합을 하면 O(N+M)

# 파인드
집합 A
집합 B
집합 C
집합 D
...

in 연잔자로 다 찾아야 함
집합이 여러개로 합치고 찾을 때
시간복잡도가 크다

반면 최적화가 된 유니온-파인드는
O(1)의 시간복잡도를 갖는 집합 알고리즘이다

즉, 파이썬의 set이 가지지 못한 장점이 있다.

"""

"""
대푯값으로 집합을 칭한다
1번노드팀(1,2,3,4), 5번노드팀(5,6,7,8), ...


유니온 
집합과 집합을 합침
대표원소가 아닌 원소로 합칠 경우 대표 원소를 찾아서 대표원소의 집합끼리 합쳐야함

파인드
대표원소를 찾는 연산
나의 번호와 부모노드의 번호가 같으면 대표원소
"""

# https://dailyalgo.kr/ko/problems/90


def solution(n, queries):
    def find(x):
        while x != parent[x]:
            x = parent[x]

        return x

    def union(x, y):
        # x가 속한 집합과 y가 속한 집합을 일단 조회(find)
        x_root = find(x)
        y_root = find(y)
        # 이미 x가 속한 집합과 y가 속한 집합이 같으면, 합집합 할 필요가 없음
        if x_root == y_root:
            return
        # x가 속한 집합과 y가 속한 집합이 다르면, 합집합
        ## parent를 집합의 번호로 바꿔주라
        ## 편의상 작은 번호 집합의 큰 번호 집합을 합친다고 정하자
        if x_root < y_root:
            parent[y_root] = x_root
        else:  # x_root > y_root
            parent[x_root] = y_root

    parent = list(range(n + 1))  # parent 배열 초기화
    answer = []

    for command, x, y in queries:
        if command == -1:
            union(x, y)
        else:
            # x와 y가 동일집합이면
            if find(x) == find(y):
                answer.append(True)
            else:
                answer.append(False)
    return answer


print(solution(5, [[-1, 3, 5], [-1, 4, 1], [-2, 4, 3], [-2, 4, 1]]))
print(
    solution(
        9,
        [
            [-1, 2, 7],
            [-2, 2, 7],
            [-2, 2, 7],
            [-1, 6, 9],
            [-1, 6, 8],
            [-1, 9, 2],
            [-1, 2, 3],
            [-2, 3, 8],
            [-1, 9, 7],
            [-2, 6, 9],
        ],
    )
)
print(
    solution(5),
    [
        [-1, 3, 5],
        [-2, 5, 1],
        [-1, 1, 5],
        [-1, 3, 5],
        [-1, 2, 5],
        [-1, 1, 2],
        [-2, 5, 4],
    ],
)
