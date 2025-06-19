# https://dailyalgo.kr/ko/problems/93

from datetime import datetime
from heapq import heappop, heappush

date_format = "%m/%d/%Y"
d1 = datetime.strptime("06/15/2026", date_format)
d2 = datetime.strptime("06/10/2026", date_format)
# print(d1 > d2)


def solution(todoList):
    heap = []
    answer = []
    priorities = {"CRITICAL": 4, "HIGH": 3, "MODERATE": 2, "LOW": 1, "MINIMAL": 0}
    for idx, todo in enumerate(todoList):
        name, due_date, priority = todo
        heappush(
            heap,
            [datetime.strptime(due_date, date_format), -priorities.get(priority), name],
        )
        if idx % 2:
            answer.append(heappop(heap)[2])

    while heap:
        answer.append(heappop(heap)[2])

    return answer


print(
    solution(
        [
            ["presentation", "11/10/2030", "HIGH"],
            ["hotfix", "11/10/2030", "CRITICAL"],
            ["laundry", "11/10/2030", "LOW"],
        ]
    )
)
