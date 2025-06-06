정점 = int(input())
간선 = int(input())

# 1. 빈 판 만들기 (정점 * 정점)
인접행렬 = [[0]*정점 for _ in range(정점)]
# print(인접행렬)
# 2. 정보 입력 받기
for _ in range(간선) :
    # 시작, 끝 = map(int, input().split())
    시작, 끝, 가중치 = map(int, input().split())
    # 인접행렬[시작][끝] = 1 # 단방향
    # 인접행렬[끝][시작] = 1 # 양방향
    인접행렬[끝][시작] = 가중치 # 단방향
    인접행렬[끝][시작] = 가중치 # 양방향

print(인접행렬)
