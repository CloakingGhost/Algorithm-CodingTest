cities = ["A", "B", "C"]
visited = [0, 0, 0]

ans = []


def perm(depth):  # 어디를 방문할지 depth로 받음
    # 종료 조건
    if depth == 3:
        print(ans)
        return
    # 다음에 갈 곳을 탐색해서
    for idx in range(3):
        # 방문한 적이 없다면
        if not visited[idx]:
            # 방문 표시하고
            visited[idx] = 1
            
            # 방문
            ans.append(cities[idx])
            perm(depth + 1)

            # 방문표시 해제, 다시방문하도록 열어둔다
            ans.pop()
            visited[idx] = 0

perm(0)
print(f'The End: {ans}')