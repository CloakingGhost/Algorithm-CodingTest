def solution(s):
    numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # "zero" ~ "nine"까지 반복하면서 있는지 찾는다.
    for name, value in numbers.items():
        s = s.replace(name, value)

    return int(s)


def solution(s):
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    # "zero" ~ "nine"까지 반복하면서 있는지 찾는다.
    for name, idx in enumerate(numbers):
        s = s.replace(name, str(idx))

    return int(s)
