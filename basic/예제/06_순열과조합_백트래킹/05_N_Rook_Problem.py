# https://www.youtube.com/watch?v=J7_UrgvTWdk&list=PLRVmiYA6hyUESim7LSzW-sVC7pBz9nMhX&index=3&t=4503s


# 재귀 -> 깊이 -> row
# visited -> column
# 한 행에 한개만 배치가능하기 때문
def solution(n):
    def permutations(row):

        nonlocal answer
        if row == n:
            answer += 1
            return

        for column in range(n):
            if row != column and not visited[column]:
                visited[column] = True
                permutations(row + 1)
                visited[column] = False

    visited = [False] * n
    answer = 0
    permutations(0)
    return answer


print(solution(2))
print(solution(3))
print(solution(5))
