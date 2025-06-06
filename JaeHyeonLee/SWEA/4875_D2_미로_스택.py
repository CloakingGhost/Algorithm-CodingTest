# region https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
'''
0 통로
1 벽
2 시작점
3 도작점

2 -> 3 갈 수 있으면 1 아니면 0 출력
'''

# endregion
T = int(input())

# 델타탐색
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for ts in range(1, T + 1):
    정점 = int(input())
    인접행렬 = [list(map(int, input().rstrip())) for _ in range(정점)]


    ans = 0
    # 예정지, 방문지
    예정지 = []
    # 방문지 = set()
    for r in range(정점):
        for c in range(정점):
            if 인접행렬[r][c] == 2:
                # 방문지.add((r, c))
                예정지.append((r, c))
                break
        if 예정지 :
            break
    
    while 예정지:
        r, c = 예정지.pop()
        if 인접행렬[r][c] == 3:
            ans = 1
            break
        인접행렬[r][c] = 1 # 방문지를 대신할 수 있음
        for n in range(4):
            nr, nc =  r + dr[n], c + dc[n]
            # if 0 <= nr < 정점 and 0 <= nc < 정점 and 인접행렬[nr][nc] != 1 and (nr, nc) not in 방문지 :
            if 0 <= nr < 정점 and 0 <= nc < 정점 and 인접행렬[nr][nc] != 1 :
                예정지.append((nr, nc))
                # 방문지.add((nr, nc))
                

    print(f"#{ts} {ans}")


# region 정리
'''
문제 풀이 한 순서
- 입력값에 대한 구조화(모든 값이 주어져 리스트로 받음)
- 시작 지점을 어떻게 찾나
- 다음 방문지를 어떻게 확인하는가
-   옆칸으로 이동하기 때문에 델타 탐색
- 델타 탐색 시 리스트 범위를 벗어나면 안됨
- 벽(1)이 아니면 다음 이동 예정지에 추가

풀이 후 개선 사항
- 방문한 곳을 벽(1)으로 만들어 중복 확인에서 제외
- 시작점 찾을 때 별도의 확인용 flag 변수 삭제
'''


# endregion