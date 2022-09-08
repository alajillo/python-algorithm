from typing import List
import collections
input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']


def solution1(input: List[str]) -> List[List[str]]:
    result = collections.defaultdict(list)
    for word in input:
        result[''.join(sorted(word))].append(word)
    print(list(result.values()))
    pass

solution1(input = input)


test = [1,100,2,3,4,5]

# test.sort(key= lambda x: -1 * x)
test.sort()
print(test)