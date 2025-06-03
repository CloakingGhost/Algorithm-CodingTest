def solution(participant, completion):
    sum_hash = sum(map(hash, participant))
    sum_hash -= sum(map(hash, completion))
    for p in participant:
        if hash(p) == sum_hash:
            return p


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
