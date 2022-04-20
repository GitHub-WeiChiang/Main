__author__ = "ChiangWei"
__date__ = "2022/04/20"

text = input('輸入一個字串：')
for letter in text:
    if letter.isupper():
        continue
    print(letter, end='')
