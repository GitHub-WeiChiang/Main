Question035 - Python 內置的 hash() 為什麼每次運作結果不同 ?
=====
* ### 要保持唯一性，请停止使用 Python 3 內置的 hash() 函數。
* ### Python 的字符串 hash 算法并不是直接遍历字符串每个字符去计算 hash，而是会額外參考一个 secret prefix 值和一个 secret suffix 值，相当于是给字符串加盐后做 hash，规避一些规律输入的情况。
* ### 这个内置 hash 函数带有随机 magic 的功能有一定的安全性上的考虑，可以让攻击者难以预测内置的 set 或者 dict 的一些行为，但远不足以承担真正的密码安全级别的 hash 的作用。
* ### 传递 set 和 dict 到其他进程的时候，只会传递其中的值，而不会传递 hash 表结构，hash 表是传到之后重新建立起来的。
* ### set 與 dict 的 hash 确实是这玩意实现的，它只保证了在同一个解释器进程里相同字符串 hash 一致。
* ### 結論: Python 的 hash() 函數只保證在同一進程下，相同的值可以獲得相同的 hash。
* ### 若需要重现可跨进程保持一致性的 hash，可以使用 hashlib 的 md5 摘要算法。
    ```
    import hashlib
    data = "時間很慢，活著很累。"
    hashlib.md5(data.encode(encoding="UTF-8")).hexdigest()
    ```
<br />
