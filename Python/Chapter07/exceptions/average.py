__author__ = "ChiangWei"
__date__ = "2022/05/03"

numbers = input('輸入數字（空白區隔）：').split(' ')
print('平均', sum(int(number) for number in numbers) / len(numbers))
