from typing import List

from common import check_solution

TEST_CASE = [{'input': list('abcdefg'), 'output': list('gfedcba')},
             {'input': list('qo32kf'), 'output': list('fk23oq')},
             {'input': list('11111111111111111'), 'output': list('11111111111111111')},
             {'input': list('bojk2ij3if'), 'output': list('fi3ji2kjob')}]


def solution1(s: List[str]) -> List[str]:
    s.reverse()
    return s

check_solution(solution1, TEST_CASE)


def solution2(s: List[str]) -> List[str]:
    s[:] = s[::-1]
    return s


check_solution(solution2, TEST_CASE)


test1 = list('test')

test2 = list('test')
# list로 list 생성 시 입력받은 문자열이 같으면 True 값으로 반환
# 저장된 메모리 주소값은 다름
print(id(test1))
print(id(test2))
print(test1 == test2)