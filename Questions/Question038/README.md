Question038 - 如何在 Python 中實作安全的型態轉換 ?
=====
* ### 當 Python 在實作型態轉換時 (str to dict, list, tuple, set, etc.)，常見的做法是透過 eval() 函數實現，但 eval() 是不安全的。
* ### 本節主角: ```ast.literal_eval()```。
* ### Example of eval()
    ```
    from typing import List

    if __name__ == '__main__':
        arr: List[str] = [
            "0", "[0]", "{0: 0}", "{0}", "__import__('os').system('ls /')"
        ]

        for i in arr:
            result = eval(i)
            print(result)

        """
        0
        [0]
        {0: 0}
        {0}
        Applications
        Library
        System
        Users
        ...
        """
    ```
    * ### eval() 除了能夠進行單純的型態轉換甚至能執行系統的命令。
    * ### 如果使用者輸入的內容是刪除文件或顯示目錄結構等命令就完蛋惹。
* ### Example of ast.literal_eval()
    ```
    import ast

    if __name__ == '__main__':
        result = ast.literal_eval("[0]")

        try:
            result = ast.literal_eval("__import__('os').system('ls /')")
        except ValueError as ve:
            print(ve)
            # malformed node or string on line 1: <ast.Call object at 0x1006fb160>
    ```
    * ### ast.literal_eval() 會判斷待解析的內容是否安全，不安全就報錯。
* ### ast.literal_eval() 是真理 !
<br />
