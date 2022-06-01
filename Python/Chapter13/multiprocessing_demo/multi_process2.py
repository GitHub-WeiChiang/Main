__author__ = "ChiangWei"
__date__ = "2022/6/1"

import multiprocessing


def foo(filename: str) -> int:
    with open(filename) as f:
        text = f.read()

    ct = 0
    for ch in text:
        n = ord(ch.upper()) + 1
        if n == 67:
            ct += 1
    return ct


if __name__ == '__main__':
    filenames = ["data1.txt", "data2.txt", "data3.txt"]
    with multiprocessing.Pool(2) as pool:
        results = [pool.apply_async(foo, (filename,)) for filename in filenames]
        count = sum(result.get() for result in results)
        print(count)
