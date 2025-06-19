# https://www.acmicpc.net/problem/16922

import sys


input = sys.stdin.readline
n = int(input())

rome_number_dict = {"I": 1, "V": 5, "X": 10, "L": 50}
rome_number = "IVXL"


def combinations_with_replacement(current, start, depth):
    if depth == n:
        if current not in numbers:
            numbers.append(current)
        return

    for i in range(start, len(rome_number)):
        current += rome_number_dict.get(rome_number[i])
        combinations_with_replacement(current, i, depth + 1)
        current -= rome_number_dict.get(rome_number[i])


numbers = []

combinations_with_replacement(0, 0, 0)
print(len(numbers))

###########################
import sys


input = sys.stdin.readline
rome_number_dict = {"I": 1, "V": 5, "X": 10, "L": 50}
rome_number = list(rome_number_dict.keys())
print(rome_number)
n = int(input())


def combinations_with_replacement(current, start):
    if len(current) == n:
        number = 0
        for sign in current:
            number += rome_number_dict.get(sign)
        if number not in numbers:
            numbers.add(number)
        return

    for i in range(start, len(rome_number)):
        current.append(rome_number[i])
        combinations_with_replacement(current, start)
        current.pop()


numbers = set()

combinations_with_replacement([], 0)
print(len(numbers))

###########################
import sys


input = sys.stdin.readline

n = int(input())
numbers = [1, 5, 10, 50]


def combinations_with_replacement(current, start):
    if len(current) == n:
        answer.add(sum(current))
        return
    for i in range(start, len(numbers)):
        current.append(numbers[i])
        combinations_with_replacement(current, i)
        current.pop()


answer = set()
combinations_with_replacement([], 0)
print(len(answer))

###########################
import sys


input = sys.stdin.readline

n = int(input())


def combinations_with_replacement(total, depth, start):
    if depth == n:
        answer.add(total)
        return

    for i in range(start, len(numbers)):
        combinations_with_replacement(total + numbers[i], depth + 1, i)


numbers = [1, 5, 10, 50]
answer = set()

combinations_with_replacement(0, 0, 0)
print(len(answer))
