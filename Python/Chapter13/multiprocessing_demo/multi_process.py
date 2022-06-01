__author__ = "ChiangWei"
__date__ = "2022/6/1"

from multiprocessing import Queue, Process


def foo(filename: str, inner_queue: Queue):
    with open(filename) as f:
        text = f.read()

    ct = 0
    for ch in text:
        n = ord(ch.upper()) + 1
        if n == 67:
            ct += 1
    inner_queue.put(ct)


if __name__ == '__main__':
    queue: Queue = Queue()
    ps = [
        Process(
            target=foo,
            args=(filename, queue)
        ) for filename in ["data1.txt", "data2.txt", "data3.txt"]
    ]
    for p in ps:
        p.start()
    for p in ps:
        p.join()

    count = 0
    while not queue.empty():
        count += queue.get()
    print(count)
