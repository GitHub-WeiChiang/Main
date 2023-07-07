Chapter02 Python 面試基礎
=====
* ### 有序數據類型如何反轉 ? 反轉函數 reverse() 與 reversed() 的區別
    ```
    from functools import reduce


    def main():
        # ---------- 字串反轉 ----------
        string: str = "abcd"

        # 切片
        print(string[::-1])

        # 遞迴
        def func_0(avg: str):
            if len(avg) < 1:
                return avg
            return func_0(avg[1:]) + avg[0]
        print(func_0(string))

        # 迴圈
        def func_1(avg: str):
            result = ""
            max_ind = len(avg) - 1
            for ind, val in enumerate(avg):
                result += avg[max_ind - ind]
            return result
        print(func_1(string))

        # 堆疊
        def func_2(avg: str):
            stack = list(avg)
            result = ""
            while len(stack) > 0:
                result += stack.pop()
            return result
        print(func_2(string))

        # reduce()
        print(reduce(lambda x, y: y + x, string))

        # reverse()
        arr = list(string)
        arr.reverse()
        print("".join(arr))

        # ---------- 陣列反轉 ----------
        array: list = [1, 2, 3, 4]

        # reversed(): 本質是一個迭代器
        print(list(reversed(array)))

        # 切片
        print(array[::-1])

        # reverse(): 直接反轉內部元素
        array.reverse()
        print(array)

        # ---------- 元組反轉 ----------
        tup: tuple = (1, 2, 3)

        # reversed(): 本質是一個迭代器
        print(tuple(reversed(tup)))

        # 切片
        print(tup[::-1])


    if __name__ == '__main__':
        main()
    ```
* ### 面向對象的接口如何實現 ?
    ```
    from abc import ABCMeta, abstractmethod


    class Interface(metaclass=ABCMeta):
        @abstractmethod
        def func_0(self):
            pass

        @abstractmethod
        def func_1(self):
            pass


    class Item(Interface):
        def func_0(self):
            print("func_0")

        def func_1(self):
            print("func_1")
    ```
* ### 繼承函數有哪幾種書寫方式 ?
    * ### 新式類
        * ### Python 3 默認使用 (繼承 Object)。
        * ### 繼承順序採用 "廣度優先" 策略。
        * ### 在 \_\_init\_\_ 中: ```super(SubClass, self).__init__(...)```。
    * ### 經典類
        * ### Python 2 默認使用 (不繼承 Object)。
        * ### 繼承順序採用 "深度優先" 策略。
        * ### 在 \_\_init\_\_ 中: ```SuperClass.__init__(self, ...)```。
* ### 可變數據類型和不可變數據類型
    * ### 不可變數據類型: 數字型 (Number)、字符串型 (String)、元組 (Tuple)。
    * ### 可變數據類型: 列表 (List)、集合 (Set)、字典 (Dictionary)。
* ### 如何判斷輸入的數是不是質數 ?
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/PythonInterview/Chapter02/eratosthenes.gif)
    ```
    import math


    # 最直接也最笨的方法
    def is_prime_1(num: int) -> bool:
        for i in range(2, num):
            if num % i == 0:
                return False

        return True


    # 将循环判断次数减少一半
    def is_prime_2(num: int) -> bool:
        limit = int(num / 2) + 1

        for i in range(2, limit):
            if num % i == 0:
                return False

        return True


    # 在法二的基础上继续提高
    def is_prime_3(num: int) -> bool:
        limit = int(math.sqrt(num)) + 1

        for i in range(2, limit):
            if num % i == 0:
                return False

        return True


    # 考虑偶数的因素
    def is_prime_4(num: int) -> bool:
        if num == 2:
            return True

        if num % 2 == 0:
            return False

        limit = int(math.sqrt(num)) + 1

        for i in range(2, limit):
            if num % i == 0:
                return False

        return True


    # 埃拉托斯特尼篩法
    def eratosthenes(n) -> list:
        temp = [True] * (n + 1)

        for i in range(2, int(n ** 0.5) + 1):
            if temp[i]:
                for j in range(i * i, n + 1, i):
                    temp[j] = False
        
        return temp


    if __name__ == '__main__':
        print(is_prime_1(9999991))
        print(is_prime_2(9999991))
        print(is_prime_3(9999991))
        print(is_prime_4(9999991))

        print()

        is_prime = eratosthenes(9999991)
        print(is_prime[9999971])
        print(is_prime[9999973])
        print(is_prime[9999991])
    ```
* ### Python 中類方法、類實例方法、靜態方法有什麼區別 ?
    ```
    class Demo:
        class_var = 0

        def __init__(self):
            self.instance_var = 1

        def instance_method(self):
            print("self.num:", self.instance_var)

        @classmethod
        def class_method(cls):
            print("cls.class_var:", cls.class_var)

        @staticmethod
        def static_method():
            print("static_method")


    if __name__ == '__main__':
        demo: Demo = Demo()
        demo.instance_method()

        Demo.class_method()

        Demo.static_method()
    ```
<br />
