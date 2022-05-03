__author__ = "ChiangWei"
__date__ = "2022/05/03"

numbers = input('輸入數字（空白區隔）：').split(' ')
try:
    ints = [int(number) for number in numbers]
except ValueError as err:
    print(err)
else:
    print('平均', sum(ints) / len(ints))
