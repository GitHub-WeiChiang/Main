Chapter05 字符串和正則表達式
=====
* ### 判斷字符串是否可以由子串重複多次構成
    ```
    def has_sub_string(string: str) -> bool:
        return string in (string + string)[1: -1]


    if __name__ == '__main__':
        # True
        print(has_sub_string("aabbccaabbcc"))
        # False
        print(has_sub_string("aabbcc"))
    ```
<br />
