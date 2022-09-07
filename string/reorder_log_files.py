from typing import List, Dict


TEST_CASE = ["dig1 8 1 5 1","let1 art can", "dig2 3 6","let2 own kit dig","let3 art zero"]


def solution(logs :List[str]) -> List[str]:
    digits = []
    letters = []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


print(solution(TEST_CASE))


def test(fuc,arg):
    print(fuc(arg))

def fuc(x):
    return x * 2

test(fuc,4)
test(lambda x: x * 2,4)