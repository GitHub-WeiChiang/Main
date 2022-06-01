__author__ = "ChiangWei"
__date__ = "2022/6/1"


def foo(inner_filename: str) -> int:
    with open(inner_filename) as f:
        text = f.read()

    ct = 0
    for ch in text:
        n = ord(ch.upper()) + 1
        if n == 67:
            ct += 1
    return ct


count = 0
for filename in ["data1.txt", "data2.txt", "data3.txt"]:
    count += foo(filename)

print(count)
