__author__ = "ChiangWei"
__date__ = "2022/5/16"

from collections import defaultdict

names = ['Justin', 'Monica', 'Irene', 'Pika', 'caterpillar']

grouped_by_len = defaultdict(list)

for name in names:
    key = len(name)
    grouped_by_len[key].append(name)

for length in grouped_by_len:
    print(length, grouped_by_len[length])
