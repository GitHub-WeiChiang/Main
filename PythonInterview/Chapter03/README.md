Chapter03 Python 中函數的應用
=====
* ### 如何生成隨機數 ?
    ```
    import random

    # 含 100
    num1 = random.randint(1, 100)
    # 不含 100
    num2 = random.randrange(1, 100)

    print(num1)
    print(num2)

    # 0 ~ 1
    num3 = random.random()
    # 0 ~ 100
    num4 = random.uniform(0, 100)

    print(num3)
    print(num4)

    """
    10
    93
    0.5059596417186859
    37.24094286081918
    """
    ```
* ### 匿名函數 lambda 的秘密
    * ### 匿名函數只有在調用時，才會創建作用域對象及函數對象。
    * ### 未調用時不佔用空間，調用時才佔用空間。
    * ### 執行完畢立即釋放，因此可以節約內存。
* ### Python 遞迴的最大層數如何實現 ?
    ```
    # 默認為 1000

    import sys
    sys.setrecursionlimit(設置上限值)
    ```
* ### 檢查輸入的字串是否是回文 (不區分大小寫) ?
    ```
    def reverse(text: str):
        return text[::-1]

    def is_hui_wen(text: str):
        text = text.lower()
        return text == reverse(text)
    ```
* ### 如何區分 filter 、map 與 reduce 函數 ?
    ```
    if __name__ == '__main__':
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        b = list(filter(lambda x: x > 5, a))
        print(b)
        # [6, 7, 8, 9]
    ```
    ```
    if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = list(map(lambda x: x * 2, a))
    print(b)
    # [2, 4, 6, 8, 10, 12, 14, 16, 18]
    ```
    ```
    from functools import reduce

    if __name__ == '__main__':
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        b = reduce(lambda x, y: x + y, a)
        print(b)
        # 45: ((((((((1 + 2) + 3) + 4) + 5) + 6) + 7) + 8) + 9)
    ```
<br />
