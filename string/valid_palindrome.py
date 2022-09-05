import collections
import re

from common import check_solution

TEST_CASE = [{'input': 'A man, a plan, a canal : Panama', 'output': True}]


def solution1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


check_solution(solution1, TEST_CASE)


def solution2(s: str) -> bool:
    strs = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


check_solution(solution2, TEST_CASE)


def solution3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]


check_solution(solution3, TEST_CASE)
