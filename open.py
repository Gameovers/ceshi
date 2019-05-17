import os
from collections import Counter


def reverse_words(string: str) -> str:
    a = list(string.split(' '))
    a.reverse()
    return " ".join(a)


s = "abc de f g"
print(reverse_words(s))

l = [
    'Lakey - Better days.mp3',
    'Wheathan - Superlove.wav',
    'groovy jam.als',
    '#4 final mixdown.als',
    'album cover.ps',
    'good nights.mp3'
]


def count_extnames(files: list) -> list:
    a = [os.path.splitext(i)[1] for i in l]
    return [item for item, count in Counter(a).items() if count > 1]


print(count_extnames(l))


