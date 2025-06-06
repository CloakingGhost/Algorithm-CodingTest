k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]


def solution(k, dungeons):
    total_dungeons = len(dungeons)

    visited = [0] * total_dungeons
    ans = -1

    def perm(depth, tired):
        nonlocal ans
        # 방문
        # 언제 멈출지 모름
        ans = max(depth, ans)
        # 탐색
        for i in range(total_dungeons):
            # 갈 수 있다면
            if not visited[i] and tired >= dungeons[i][0]:
                # 바로 방문 체크
                visited[i] = 1
                # 방문
                perm(depth + 1, tired - dungeons[i][1])
                # 방문 체크 해제
                visited[i] = 0

    perm(0, k)

    return ans


from itertools import permutations


def solution(k, dungeons):
    answer = -1
    # 던전들의 모든 조합이 담겨있음
    for each_case in permutations(dungeons):
        cnt = 0
        tmp_k = k
        # 던전들의 정보가 담겨있음
        for dungeon in each_case:
            if tmp_k >= dungeon[0]:
                tmp_k -= dungeon[1]
                cnt += 1
            else:
                break

        answer = max(cnt, answer)

    return answer


print(solution(k, dungeons))
