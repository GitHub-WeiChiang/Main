__author__ = "ChiangWei"
__date__ = "2022/5/16"

names = ['Justin', 'Monica', 'Irene', 'Pika', 'caterpillar']

grouped_by_len = {}
for name in names:
    key = len(name)
    if key not in grouped_by_len:
        grouped_by_len[key] = []
    grouped_by_len[key].append(name)

for length in grouped_by_len:
    print(length, grouped_by_len[length])
