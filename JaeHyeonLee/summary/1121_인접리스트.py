정점 = int(input())
간선 = int(input())

# 1. 빈 판 만들기 ([] * 정점)
인접리스트 = [[] for _ in range(정점)]
# print(인접리스트)
# 2. 정보 입력 받기
for _ in range(간선) :
    # 시작, 끝 = map(int, input().split())
    시작, 끝, 가중치 = map(int, input().split())
    # 인접리스트[시작].append(끝) # 단방향
    # 인접리스트[끝].append(시작) # 양방향
    인접리스트[시작].append((끝, 가중치)) # 단방향
    인접리스트[끝].append((시작, 가중치)) # 양방향
    
    
    
    

print(인접리스트)
