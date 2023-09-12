Question048 - Python 中 if \_\_name\_\_ == '\_\_main\_\_': 的作用為何 ?
=====
* ### 在每次執行代碼前，Python 解釋器首先會讀取工程師所撰寫的原文件，並自動定義一些特殊的全局變量 (可以透過 ```print(dir())``` 查看)。
* ### 示例代碼
    ```
    # script_1.py

    print(f"{__name__ = }")
    ```
    ```
    python script_1.py
    # __name__ = '__main__'
    ```
    ```
    # script_2.py

    import script_1
    ```
    ```
    python script_2.py
    # __name__ = 'script_1'
    ```
* ### 每一個 Python 文件都可以作為一個單獨的腳本進行運行，也可以作為一個模塊被其它腳本引入，變量 ```__name__``` 可以用於判斷當前是哪一種情況。
* ### 示例代碼
    ```
    # script_1.py

    def add(a: int, b: int) -> None:
        print(f"{a} + {b} = {a+b}")

    add(3, 4)
    ```
    ```
    python script_1.py
    3 + 4 = 7
    ```
    ```
    # script_2.py

    from script_1 import add

    add(1, 1)
    ```
    ```
    python script_2.py
    3 + 4 = 7
    1 + 1 = 2
    ```
* ### 解決方法 (修改 script_1.py)
    ```
    # script_1.py

    def add(a: int, b: int) -> None:
        print(f"{a} + {b} = {a+b}")

    if __name__ == "__main__":
        add(3, 4)
    ```
    ```
    python script_2.py
    1 + 1 = 2
    ```
* ### 代碼 ```if __name__ == "__main__":``` 表示: 用於判斷是否正在運行當前腳本，若是則會執行後續的測試代碼，否則代表當前腳本被作為模塊所導入，測試代碼將不會被執行。
* ### 理解更多 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/Python)
<br />
