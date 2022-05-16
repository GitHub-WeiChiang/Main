__author__ = "ChiangWei"
__date__ = "2022/5/16"

from collections import defaultdict
from operator import itemgetter


def count(inner_text):
    counter = defaultdict(int)
    for inner_c in inner_text:
        counter[inner_c] += 1
    return counter.items()


text = 'Your right brain has nothing left.'
for c, n in sorted(count(text), key=itemgetter(0)):
    print(c, ':', n)
