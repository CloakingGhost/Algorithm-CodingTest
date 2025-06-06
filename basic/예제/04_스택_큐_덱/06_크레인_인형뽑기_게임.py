# https://school.programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    for move in moves:
        for i in range(n):
            doll_num = board[i][move - 1]
            if doll_num:
                board[i][move - 1] = 0
                if stack and stack[-1] == doll_num:
                    stack.pop()
                    answer += 2
                    break
                stack.append(doll_num)
                break

    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
