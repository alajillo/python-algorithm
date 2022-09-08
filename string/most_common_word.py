import re, collections
paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'

banned = ['hit']

def solution1(paragraph,banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

def solution2(paragraph,banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1
    return max(counts, key= counts.get)


print(solution1( banned = banned, paragraph = paragraph))
print(solution2( banned = banned, paragraph = paragraph))


