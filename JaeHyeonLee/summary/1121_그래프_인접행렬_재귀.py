# region 인접행렬 + 재귀

"""
방문예정지 없어도 됨

"""


# endregion

# region 구현
정점, 간선 = map(int, input().split()) # 개수

인접행렬 = [[0] * (정점 + 1) for _ in range(정점 + 1)]

# 간선 개수 만큼
for _ in range(간선):
    시작, 끝 = map(int, input().split())
    인접행렬[시작][끝] = 1
    인접행렬[끝][시작] = 1

# 세팅
방문지 = set()
궤적 = []

# 탐색, 재귀
def 깊이우선탐색(현재_정점):
    if 현재_정점 not in 방문지:
        궤적.append(현재_정점)
    방문지.add(현재_정점)
    
    for 다음_정점 in range(정점 + 1):
         # 1이면 연결되어 있음
        if 인접행렬[현재_정점][다음_정점] and 다음_정점 not in 방문지:
            깊이우선탐색(다음_정점) # 시스템 스택에 쌓이기 때문
        
깊이우선탐색(1) # 1번 정점과 연결된 정점을 모은다

print(궤적)



# endregion
