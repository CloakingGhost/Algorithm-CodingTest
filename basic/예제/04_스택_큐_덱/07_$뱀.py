# https://www.notion.so/1d1611ac3a0080c19460e741c49f4cdf?p=1de611ac3a00803a97f9db1264541a7c&pm=s
import sys
from collections import deque

input = sys.stdin.readline

EMPTY, BODY, APPLE = 0, 1, 2
# 보드
n = int(input())
board = [[EMPTY] * n for _ in range(n)]

# 사과
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = APPLE  # 인덱스 위치가 아님

# 방향 변환 정보
l = int(input())
turn_info = {}
for _ in range(l):
    x, c = input().split()
    turn_info[int(x)] = c

# 델타: 우 하 좌 상
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0  # 방향 (우향)

# 게임 시작
snake = deque([(0, 0)])  # 시작 위치
board[0][0] = BODY
time = 0
while True:
    time += 1
    # 다음 이동 위치
    hx, hy = snake[-1]  # 머리 위치
    nx, ny = hx + dx[direction], hy + dy[direction]
    # 탈출 조건: 범위(벽), 자신과 충돌
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == BODY:
        break

    # 머리 위치 추가
    snake.append((nx, ny))
    is_apple = board[nx][ny] == APPLE
    board[nx][ny] = BODY  # 아래에 있어야 사과인지 확인 가능

    # 사과 아니면 꼬리 위치 제거
    if not is_apple:
        tx, ty = snake.popleft()  # tail: x, y
        board[tx][ty] = EMPTY

    # 매순간 방향 전환 확인
    turn = turn_info.get(time)  # O(1)
    if turn == "L":
        direction = (direction - 1) % 4
    elif turn == "D":
        direction = (direction + 1) % 4

print(time)
"""
❌ 실수: 사과 좌표가 1-index인데 0-index 변환 안 함
🧠 교훈: 좌표 입력 받을 땐 항상 -1 여부 먼저 체크
✔️ 해결 방법: board[r-1][c-1]로 수정

❌ 실수: 변수 이름을 구체적으로 작성하지 않음
🧠 교훈: 의미를 담아서 작성
✔️ 해결 방법: d => direction

❌ 실수: 코드 실행 순서 고려하지 않음
🧠 교훈: 생각의 흐름을 이용하려면 변수를 작성
✔️ 해결 방법: is_apple = board[nx][ny] == APPLE 만들어서 조건문에 사용
"""
