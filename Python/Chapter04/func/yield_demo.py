__author__ = "ChiangWei"
__date__ = "2022/04/21"

def xrange(n):
    x = 0
    while x != n:
        yield x
        x += 1

for n in xrange(10):
    print(n)
